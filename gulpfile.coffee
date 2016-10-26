g = require "gulp"
toolbox = require "hyamamoto-job-toolbox"
path = require "path"

modules =
  "common": "app/common"

for name, mod_path of modules
  do (name, modPath) ->
    destPath = path.join(modPath, "jinja2")
    toolbox.coffee(
      "#{name}.", modPath, destPath,
      undefined, undefined, undefined, undefined, name
    )
    toolbox.sass "#{name}.", path, destPath, name
