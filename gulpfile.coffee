g = require "gulp"
require "./gulp/backend"

default_dependencies = []
if process.env.CI
  default_dependencies.concat [
    "check.backend"
  ]
g.task "default", default_dependencies, ->
  if not process.env.CI
    g.watch "app/**/*.py", ["check.backend"]
