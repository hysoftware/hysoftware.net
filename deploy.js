/* eslint no-console: ["error", { allow: ["log", "warn", "error"] }] */

((require) => {
  const https = require('https');
  const qs = require('querystring');
  const url = require('url');
  const fs = require('fs');
  const mime = require('mime-types');
  const q = require('q');

  const releaseArtifact = process.argv.splice(2, 1);

  const releaseBody = JSON.stringify({ tag_name: process.env.CIRCLE_TAG });
  const releaseOpt = url.parse(
    'https://api.github.com/repos/hysoftware/hysoftware.net/releases'
  );
  releaseOpt.method = 'POST';
  releaseOpt.auth =
    `${process.env.RELEASE_USER_NAME}:${process.env.RELEASE_TOKEN}`;
  releaseOpt.headers = {
    'Content-Type': 'application/json',
    'Content-Length': releaseBody.length,
  };

  q.fcall(() => {
    if (!(
      process.env.CIRCLE_TAG &&
      process.env.RELEASE_USER_NAME &&
      process.env.RELEASE_TOKEN
    )) {
      throw new Error(
        `MUST have proper environemnt arguments:
        CIRCLE_TAG, RELEASE_USER_NAME, RELEASE_TOKEN`);
    }
    if (!releaseArtifact.length) {
      throw new Error('File name to deploy is needed');
    }
  }).then(() => {
    const defer = q.defer();
    const req = https.request(
      releaseOpt, (res) => {
        res.setEncoding('utf-8');
        let raw = '';
        res.on('data', (chunk) => { raw += chunk; });
        res.on('end', () => {
          try {
            if (!(res.statusCode >= 200 && res.statusCode < 300)) {
              defer.reject(
                new Error(`${res.statusCode}: ${res.statusMessage}, ${raw}`)
              );
              return;
            }
            defer.done(JSON.parse(raw));
          } catch (e) {
            defer.reject(e);
          }
        });
      }).on('error', defer.reject);
    req.write(releaseBody);
    req.end();
    return defer.promise;
  }).then((parse) => {
    const targetFile = fs.createReadStream(releaseArtifact[0]);
    return q.nfcall(
      fs.stat, targetFile.path
    ).then(stat => [
      targetFile, stat, parse,
    ]);
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
    const post = https.method(uploadUrl, (res) => {
      let raw = '';
      res.on('data', (chunk) => { raw += chunk; });
      res.on('end', () => {
        if (!(res.statusCode >= 200 && res.statusCode < 300)) {
          postPromise.reject(
            new Error(`${res.statusCode}: ${res.statusMessage}, ${raw}`)
          );
        }
        console.log('Done.');
        targetFile.close();
        postPromise.resolve();
      });
    }).on('error', postPromise.reject);
    targetFile.pipe(post);
    post.end();
    return postPromise.promise;
  })
  .catch((e) => {
    console.error(e);
    throw e;
  });
})(require);
