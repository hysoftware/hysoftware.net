path = require "path"

g = require "gulp"
toolbox = require "hyamamoto-job-toolbox"

plumber = require "gulp-plumber"
notify = require "gulp-notify"

uglify = require "gulp-uglify"
concat = require "gulp-concat"
sourcemaps = require "gulp-sourcemaps"

q = require "q"
rimraf = require "rimraf"

g.task "third_party", ->
  prefix = "app/common/static/third_party"
  files = (path.join(prefix, item) for item in [
    "angular/angular.js"
    "angular-animate/angular-animate.js"
    "angular-aria/angular-aria.js"
    "angular-messages/angular-messages.js"
    "angular-resource/angular-resource.js"
    "angular-material/angular-material.js"
  ])

  pipe = g.src(files).pipe(
    plumber "errorHandler": notify.onError '<%= error.message %>'
  )
  if not toolbox.helper.isProduction
    pipe = pipe.pipe sourcemaps.init()
  pipe = pipe.pipe(concat("third_party.js")).pipe uglify()
  if not toolbox.helper.isProduction
    pipe = pipe.pipe sourcemaps.write()
  pipe.pipe g.dest "app/common/static"

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

toolbox.python "", "app", undefined, undefined, undefined, ["app/*/migrations"]

g.task "django.test", ["python.mentain"], ->
  q.nfcall(rimraf, "app/**/?(*.pyc|__pycache__)").then(
    -> toolbox.virtualenv(
      "coverage erase"
    )
  ).then(
    -> toolbox.virtualenv(
      "DJANGO_SETTINGS_FACTORY='app.settings.testing.TestConfig'
       RECAPTCHA_TESTING='True'
       coverage run --branch --omit '*/migrations/*'
       --source=app -- manage.py test"
    )
  ).then(-> toolbox.virtualenv("coverage report -m "))

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
