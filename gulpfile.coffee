path = require "path"

http = require "http"
qs = require "querystring"
url = require "url"
fs = require "fs"
mime = require "mime-types"
colors = require "colors"

g = require "gulp"
toolbox = require "hyamamoto-job-toolbox"
command = require "simple-process"

plumber = require "gulp-plumber"
notify = require "gulp-notify"

uglify = require "gulp-uglify"
concat = require "gulp-concat"
sourcemaps = require "gulp-sourcemaps"
webpack = require "webpack"

q = require "q"
rimraf = require "rimraf"

g.task "third_party", ->
  q.nfcall(
    webpack, require(
      path.resolve(path.join(__dirname, 'third_party', 'webpack.conf.js'))
    )
  ).then((stats) ->
    console.log stats.toString({
      "colors": true,
      "chunks": false
    })
  ).catch plumber(errorHandler: notify.onError '<%= error.message %>')

modules = ["common", "home", "legal", "user"]

for name in modules
  do (name) ->
    g.task "#{name}.webpack", ->
      q.nfcall(
        webpack, require(
          path.resolve(path.join(__dirname, "app", name, 'webpack.conf.js'))
        )
      ).then((stats) ->
        console.log stats.toString({
          "colors": true,
          "chunks": false
        })
      ).catch plumber(errorHandler: notify.onError '<%= error.message %>')

toolbox.python "", "app", [], undefined, undefined, ["app/*/migrations"]

g.task "django.test", ["python.mentain"], ->
  q.nfcall(rimraf, "app/**/?(*.pyc|__pycache__)").then(-> command.pyvenv(
    "coverage erase", [], undefined, ("stdio": ["pipe", "inherit", "inherit"]))
  ).then(-> command.pyvenv(
    "DJANGO_SETTINGS_FACTORY='app.settings.testing.TestConfig'
     RECAPTCHA_TESTING='True' coverage run --branch --omit '*/migrations/*'
     --source=app -- manage.py test", [], undefined,
     ("stdio": ["pipe", "inherit", "inherit"])
  )).then(-> command.pyvenv(
    "coverage report -m", [], undefined,
    ("stdio": ["pipe", "inherit", "inherit"])
  ))

g.task "upload.githubRelease", ->
  errHandler = plumber(errorHandler: notify.onError '<%= error.message %>')
  q.nfcall(
    ->
      if not (
        process.env.CIRCLE_TAG and
        process.env.RELEASE_USER_NAME and
        process.env.RELEASE_TOKEN
      )
        throw new Error(
          "MUST have proper environemnt arguments:
            CIRCLE_TAG, RELEASE_USER_NAME, RELEASE_TOKEN"
        )
      if not process.argv[2]
        throw new Error("File name to deploy is needed")
  ).then(
    ->
      http.get(
        "https://api.github.com/repos/hysoftware/\
         hysoftware.net/releases/tags/#{process.env.CIRCLE_TAG}",
        (res) ->
          if not (200 <= res.statusCode < 300)
            q.reject(new Error("#{res.statusCode}: #{res.statusMessage}"))
          res.setEncoding("utf-8")
          raw = ''
          res.on("data", (chunk) -> raw += chunk)
          res.on("end", ->
            try
              prase = JSON.parse(raw)
              ret.done(parse)
            catch e
              ret.reject(e)
          )
       ).on("error", ret.reject)
      return ret
  ).then(
    (parse) ->
      ret = q.defer()
      targetFile = fs.createReadStream(process.argv[2])
      q.nfcall(fs.stat, targetFile.path).then(
        (stat) -> ret.done([targetFile, stat, parse])
      ).catch(ret.reject)
      return ret
  ).then(
    (value) ->
      ret = q.defer()
      [targetFile, stat, parse] = value
      uploadUrl = url.parse(parse.uploadUrl.replace(
        /\{\?name\,label\}$/g,
        "?" + qs.stringify({name: targetFile.path})
      ))
      uploadUrl.method = "POST"
      uploadUrl.auth = "#{RELEASE_USER_NAME}:#{RELEASE_TOKEN}"
      uploadUrl.headers = {
        "Content-Type": mime.lookup(targetFile.path),
        "Content-Length": stat.size
      }
      post = http.method(uploadUrl, (res) ->
        if not (200 <= res.statusCode < 300)
          ret.reject(new Error("#{res.statusCode}: #{res.statusMessage}"))
        res.on("end", ->
          console.log("Done!".green)
          readable.close()
          q.done()
        )
      ).on("error", ret.reject)
      readable.pipe(post)
      return ret
  ).catch((e) -> errorHandler(e))

init_deps = []

if toolbox.helper.isProduction or process.env.node_mode is "init"
  init_deps = init_deps.concat(
    "third_party"
    ("#{name}.webpack" for name in modules)
    "django.test"
  )

g.task "default", init_deps, ->
  if not toolbox.helper.isProduction
    for mod_name in modules
      do (mod_name) ->
        g.watch [
          path.join("app", mod_name, "**/coffee/**/*.coffee"),
          path.join("app", mod_name, "**/*.scss"),
          path.join("app", mod_name, "main.js")
        ], ["#{mod_name}.webpack"]
    g.watch ["app/**/*.py", "tests/**/*.py"], ["django.test"]
