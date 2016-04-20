g = require "gulp"
thirdParty = require "./gulp/third_party"
require("gulp-help")(g)

toolbox = require "hyamamoto-job-toolbox"
toolboxHelper = require "hyamamoto-job-toolbox/lib/helper"

toolbox.karma(
  "", "app", thirdParty.thirdPartyPackages.concat([
    "#{thirdParty.thirdPartyPrefix}/angular-mocks/angular-mocks.js"
  ]), ["static"]
)
toolbox.coffee "", "app", "./app/home/assets", [], ["karma.runner"]
toolbox.selfcheck.coffee "", "./etc/coffeelint.json"
toolbox.less "", "app", "./app/home/assets"
toolbox.python "", "app", [
  "--with-coverage", "--cover-erase", "--cover-package=app", "--all"
]

default_dependencies = [
  "selfcheck"
  "check.backend"
  "third_party"
  "frontend.less"
  "frontend.coffee"
] if toolboxHelper.isProduction or process.env.mode is "init"
default_dependencies = [
  "karma.server"
] if not (toolboxHelper.isProduction or process.env.mode is "init")

g.task "default", default_dependencies or [], ->
  if not (toolboxHelper.isProduction or process.env.mode is "init")
    g.watch ["tests/**/*.py", "app/**/*.py"], ["python.nosetest"]
    g.watch ["./gulpfile.coffee", "./gulp/**/*.coffee"], [".selfcheck.coffee"]
    g.watch ["./gulp/third_party.coffee"], ["third_party"]
    g.watch ["app/**/less/**/*.less", "app/main.less"], ["less"]
    g.watch [
      "app/**/coffee/**/*.coffee",
      "app/main.coffee",
      "tests/**/coffee/**/*.coffee"
    ], ["coffee"]
