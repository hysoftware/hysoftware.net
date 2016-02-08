g = require "gulp"
require "./gulp/backend"
require "./gulp/selfcheck"

default_dependencies = []
if process.env.CI
  default_dependencies.concat [
    "check.backend"
    "selfcheck"
  ]
g.task "default", default_dependencies, ->
  if not process.env.CI
    g.watch "app/**/*.py", ["check.backend"]
    g.watch ["./gulpfile.coffee", "./gulp/**/*.coffee"], ["selfcheck"]
