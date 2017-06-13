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

modules =
  "common": "app/common"
  "home": "app/home"
  "legal": "app/legal"
  "user": "app/user"

for name, modPath of modules
  do (name, modPath) ->
    destPath = path.join(modPath, "jinja2")
    toolbox.coffee(
      "#{name}.", modPath, destPath,
      undefined, undefined, undefined, undefined, undefined, name, false
    )
    toolbox.sass "#{name}.", modPath, destPath, name

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
    ("#{name}.coffee" for name in Object.keys modules)
    ("#{name}.scss" for name in Object.keys modules)
    "django.test"
  )

g.task "default", init_deps, ->
  if not toolbox.helper.isProduction
    for mod_name, prefix of modules
      do (mod_name, prefix) ->
        g.watch [path.join(prefix, "**/*.scss")], ["#{mod_name}.scss"]
        g.watch [
          path.join(prefix, "**/coffee/**/*.coffee")
        ], ["#{mod_name}.coffee"]
    g.watch ["app/**/*.py", "tests/**/*.py"], ["django.test"]
