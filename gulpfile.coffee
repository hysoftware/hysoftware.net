g = require "gulp"
require "./gulp/backend"
require "./gulp/selfcheck"
require "./gulp/third_party"

default_dependencies = if process.env.CI or process.env.mode is "init" then [
  "selfcheck"
  "check.backend"
  "third_party"
] else []

g.task "default", default_dependencies, ->
  if process.env.CI
    process.env.mode = "production"
    g.start "third_party"
  else if process.env.mode not in ["production", "init"]
    g.watch "app/**/*.py", ["check.backend"]
    g.watch ["./gulpfile.coffee", "./gulp/**/*.coffee"], ["selfcheck"]
