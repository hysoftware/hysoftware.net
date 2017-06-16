path = require "path"

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
