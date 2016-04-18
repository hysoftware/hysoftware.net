g = require "gulp"
require("gulp-help")(g)

toolbox = require "hyamamoto-job-toolbox"

# require "./gulp/backend"
# require "./gulp/selfcheck"
# require "./gulp/third_party"
# require "./gulp/frontend"

toolbox.coffee "", "app", "./home/assets"
toolbox.selfcheck.coffee "", "./etc/coffeelint.json"
toolbox.less "", "app", [], "./home/assets"
toolbox.python "", "app"

default_dependencies = [
  "selfcheck"
  "check.backend"
  "third_party"
  "frontend.less"
  "frontend.coffee"
] if process.env.CI or process.env.node_mode in ["init", "production"]

g.task "default", default_dependencies or [], ->
  if process.env.node_mode not in ["production", "init"]
    g.watch ["tests/**/*.py", "app/**/*.py"], ["check.backend"]
    g.watch ["./gulpfile.coffee", "./gulp/**/*.coffee"], ["selfcheck"]
    g.watch ["./gulp/third_party.coffee"], ["third_party"]
    g.watch ["app/**/less/**/*.less", "app/main.less"], ["frontend.less"]
    g.watch [
      "app/**/coffee/**/*.coffee"
      "app/main.coffee"
    ], [
      "frontend.coffee"
    ]
