/* eslint no-console: ["error", { allow: ["log", "warn", "error"] }] */
/* eslint no-restricted-syntax: [
  "error", "FunctionExpression", "WithStatement",
] */
((r) => {
  const path = r('path');

  const http = r('http');
  const qs = r('querystring');
  const url = r('url');
  const fs = r('fs');
  const mime = r('mime-types');

  const g = r('gulp');
  const toolbox = r('hyamamoto-job-toolbox');
  const command = r('simple-process');

  const plumber = r('gulp-plumber');
  const notify = r('gulp-notify');

  const webpack = r('webpack');

  const q = r('q');
  const rimraf = r('rimraf');

  const errorHandler = plumber({
    errorHandler: notify.onError('<%= error.message %>'),
  });

  const makeWebPack = (webpackPath) => {
    const packPromise = q.nfcall(webpack, r(webpackPath)).then((stats) => {
      console.log(stats.toString({
        colors: true,
        chunks: false,
      }));
    }).catch(errorHandler);
    return packPromise;
  };

  g.task('third_party', () => {
    const pack = makeWebPack(
      path.resolve(path.join(__dirname, 'third_party', 'webpack.conf.js'))
    );
    return pack;
  });

  const modules = ['common', 'home', 'legal', 'user'];
  for (const n of modules) {
    ((name) => {
      g.task(`${name}.webpack`, () => {
        const webpackPath =
          path.resolve(path.join(__dirname, 'app', name, 'webpack.conf.js'));
        return makeWebPack(webpackPath);
      });
    })(n);
  }

  toolbox.python('', 'app', [], undefined, undefined, ['app/*/migrations']);

  g.task('django.test', ['python.mentain'], () => {
    const taskPromise = q.nfcall(
      rimraf,
      'app/**/?(*.pyc|__pycache__)'
    ).then(() => {
      const ret = command.pyvenv('coverage erase', [], undefined, {
        stdio: ['pipe', 'inherit', 'inherit'],
      });
      return ret;
    }).then(() => {
      const ret = command.pyvenv(
        `DJANGO_SETTINGS_FACTORY='app.settings.testing.TestConfig'
         RECAPTCHA_TESTING='True' coverage run --branch \
         --omit '*/migrations/*' --source=app -- manage.py test`,
         [], undefined, {
           stdio: ['pipe', 'inherit', 'inherit'],
         });
      return ret;
    }).then(() => {
      const ret = command.pyvenv(
        'coverage report -m', [], undefined, {
          stdio: ['pipe', 'inherit', 'inherit'],
        });
      return ret;
    });
    return taskPromise;
  });

  g.task('upload.githubRelease', () => {
    const ret = q.nfcall(() => {
      if (!(
        process.env.CIRCLE_TAG &&
        process.env.RELEASE_USER_NAME &&
        process.env.RELEASE_TOKEN
      )) {
        throw new Error(
          `MUST have proper environemnt arguments:
          CIRCLE_TAG, RELEASE_USER_NAME, RELEASE_TOKEN`);
      }
      if (!process.argv[2]) {
        throw new Error('File name to deploy is needed');
      }
    }).then(() => {
      const defer = q.defer();
      http.get(
        `https://api.github.com/repos/hysoftware/\
         hysoftware.net/releases/tags/${process.env.CIRCLE_TAG}`,
        (res) => {
          if (!(res.statusCode >= 200 && res.statusCode < 300)) {
            defer.reject(new Error(`${res.statusCode}: ${res.statusMessage}`));
          }
          res.setEncoding('utf-8');
          let raw = '';
          res.on('data', (chunk) => { raw += chunk; });
          res.on('end', () => {
            try {
              defer.done(JSON.parse(raw));
            } catch (e) {
              defer.reject(e);
            }
          });
        }).on('error', ret.reject);
      return defer.promise;
    }).then((parse) => {
      const defer = q.defer();
      const targetFile = fs.createReadStream(process.argv[2]);
      q.nfcall(fs.stat, targetFile.path).then((stat) => {
        defer.done([targetFile, stat, parse]);
      }).catch(defer.reject);
      return defer.promise;
    }).then((value) => {
      const postPromise = q.defer();
      const [targetFile, stat, parse] = value;
      const uploadUrl = url.parse(parse.uploadUrl.replace(
        /\{\?name,label\}$/g,
        `?${qs.stringify({ name: targetFile.path })}`
      ));
      uploadUrl.method = 'POST';
      uploadUrl.auth =
      `${process.env.RELEASE_USER_NAME}:${process.env.RELEASE_TOKEN}`;
      uploadUrl.headers = {
        'Content-Type': mime.lookup(targetFile.path),
        'Content-Length': stat.size,
      };
      const post = http.method(uploadUrl, (res) => {
        if (!(res.statusCode >= 200 && res.statusCode < 300)) {
          postPromise.reject(
            new Error(`${res.statusCode}: ${res.statusMessage}`)
          );
        }
        res.on('end', () => {
          console.log('Done.');
          targetFile.close();
          postPromise.resolve();
        });
      }).on('error', postPromise.reject);
      targetFile.pipe(post);
      return postPromise.promise;
    })
    .catch(errorHandler);
    return ret;
  });

  const initDeps = [];
  if (toolbox.helper.isProduction || process.env.node_mode === 'init') {
    initDeps.push('third_party');
    for (const n of modules) {
      ((name) => {
        initDeps.push(`${name}.webpack`);
      })(n);
    }
    initDeps.push('django.test');
  }
  g.task('default', initDeps, () => {
    if (!toolbox.helper.isProduction) {
      for (const n of modules) {
        ((name) => {
          g.watch([
            path.join('app', name, '**/coffee/**/*.coffee'),
            path.join('app', name, '**/es6/**/*.es6'),
            path.join('app', name, '**/*.scss'),
            path.join('app', name, 'main.js'),
          ], [`${name}.webpack`]);
        })(n);
      }
      g.watch(['app/**/*.py', 'tests/**/*.py'], ['django.test']);
    }
  });
})(require);
