/* eslint no-console: ["error", { allow: ["log", "warn", "error"] }] */
/* eslint no-restricted-syntax: [
  "error", "FunctionExpression", "WithStatement",
] */
((r) => {
  const path = r('path');
  const _ = r('lodash');

  const g = r('gulp');
  const toolbox = r('hyamamoto-job-toolbox');
  const { webpack: Webpack, python: Python } = toolbox;
  const command = r('simple-process');

  const q = r('q');
  const rimraf = r('rimraf');

  g.on('error', (err) => {
    if (!_.isEmpty(err)) {
      if (err.stats) {
        console.error(err.stats);
      }
      toolbox.helper.notifyError(err.error);
    }
  });

  const adjustWebpackEntries = (modulePath, webPackEntries) => {
    const entries = _.cloneDeep(webPackEntries);
    Object.entries(entries).forEach((el) => {
      const [key, scriptPath] = el;
      entries[key] =
        path.resolve(__dirname, path.join(modulePath, scriptPath));
    });
    return entries;
  };

  g.registry(new Webpack(
    adjustWebpackEntries(
      path.resolve(path.join(__dirname, 'third_party')),
      r('./third_party/packfile.json')
    ),
    'app/common',
    {
      taskPrefix: 'third_party.',
      webPackConfigToMerge: {
        mode: 'production',
        resolve: {
          modules: [
            path.resolve(path.join(
              __dirname,
              'third_party',
              'bower_components'
            )),
            path.resolve(path.join(__dirname, 'node_modules')),
          ],
        },
      },
    }
  ));

  const modules = [
    ['common', 'jinja2'],
    ['home', 'static'],
    ['legal', 'static'],
    ['user', 'jinja2'],
  ];
  for (const [name, outPath] of modules) {
    g.registry(new Webpack(
      adjustWebpackEntries(
        path.join(__dirname, 'app', name),
        r(`./app/${name}/packfile.json`)
      ),
      path.join(__dirname, 'app', name),
      {
        outPath,
        taskPrefix: `${name}.`,
        webPackConfigToMerge: {
          mode: 'production',
        },
      }
    ));
  }

  g.registry(new Python('app', { additionalExclude: ['app/*/migrations'] }));

  g.task('django.test', g.series(
    'python.syntax',
    'python.complex',
    'python.maintain',
    () => {
      const taskPromise = q.nfcall(
        rimraf,
        'app/**/?(*.pyc|__pycache__)'
      ).then(() => {
        const ret = command.pyvenv('coverage erase', [], undefined, {
          stdio: ['pipe', 'inherit', 'inherit'],
        });
        return ret;
      }).then(() => {
        process.env.DJANGO_SETTINGS_FACTORY = 'app.settings.testing.TestConfig';
        process.env.RECAPTCHA_TESTING = 'True';
        const ret = command.pyvenv(
          [
            'coverage run --branch --omit \'*/migrations/*\' ',
            '--source=app -- manage.py test',
          ].join(' '),
          [], undefined, { stdio: ['pipe', 'inherit', 'inherit'] }
        );
        delete process.env.DJANGO_SETTINGS_FACTORY;
        delete process.env.RECAPTCHA_TESTING;
        return ret;
      }).then(() => command.pyvenv('coverage report -m', [], undefined, {
        stdio: ['pipe', 'inherit', 'inherit'],
      }));
      return taskPromise;
    }
  ));

  g.task('watch', () => {
    for (const [name] of modules) {
      g.watch([
        path.join('app', name, '**/coffee/**/*.coffee'),
        path.join('app', name, '**/es6/**/*.es6'),
        path.join('app', name, '**/*.scss'),
        path.join('app', name, 'main.js'),
      ], g.series(`${name}.webpack`));
    }
    g.watch([
      'app/**/*.py',
      'app/**/jinja2/**/*.html',
      'tests/**/*.py',
    ], g.series('django.test'));
  });
  const defaultTasks =
    (toolbox.helper.isProduction || process.env.node_mode === 'init') ?
      g.parallel.apply(
        g.parallel,
        ['third_party.webpack']
          .concat(modules.map(item => `${item[0]}.webpack`))
      ) : g.series('watch');
  g.task('default', defaultTasks);
})(require);
