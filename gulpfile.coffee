g = require "gulp"
coveralls = require "gulp-coveralls"
thirdParty = require "./gulp/third_party"
require("gulp-help")(g)

toolbox = require "hyamamoto-job-toolbox"
karmaConf = require "./etc/karma.conf"
toolboxHelper = require "hyamamoto-job-toolbox/lib/helper"

toolbox.karma(
  "", "app", thirdParty.thirdPartyPackages.concat([
    "#{thirdParty.thirdPartyPrefix}/angular-mocks/angular-mocks.js"
  ]), ["static"], karmaConf
)
toolbox.coffee "", "app", "./app/home/assets", [], [
  if toolboxHelper.isProduction or process.env.node_mode is "init"
    "karma.server"
  else
    "karma.runner"
]
toolbox.selfcheck.coffee "", "./etc/coffeelint.json"
toolbox.less "", "app", "./app/home/assets"
toolbox.python "", "app", [
  "--with-coverage", "--cover-erase", "--cover-package=app", "--all"
]

default_dependencies = []
if toolboxHelper.isProduction or process.env.node_mode is "init"
  default_dependencies = [
    ".selfcheck.coffee"
    "python.nosetest"
    "third_party"
    "less"
    "coffee"
  ]
else
  default_dependencies = ["karma.server"]

g.task "default", default_dependencies or [], ->
  if not (toolboxHelper.isProduction or process.env.node_mode is "init")
    g.watch ["tests/**/*.py", "app/**/*.py"], ["python.nosetest"]
    g.watch ["./gulpfile.coffee", "./gulp/**/*.coffee"], [".selfcheck.coffee"]
    g.watch ["./gulp/third_party.coffee"], ["third_party"]
    g.watch ["app/**/less/**/*.less", "app/main.less"], ["less"]
    g.watch [
      "app/**/coffee/**/*.coffee",
      "app/main.coffee",
      "tests/**/coffee/**/*.coffee"
    ], ["coffee"]

g.task "coveralls", ->
  g.src("frontend_coverages/**/lcov.info").pipe coveralls()
