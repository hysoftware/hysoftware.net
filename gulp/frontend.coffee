g = require "gulp"
rename = require "gulp-rename"
prefixer = require "gulp-autoprefixer"
less = require "gulp-less"
LessCleanCss = require "less-plugin-clean-css"
plumber = require "gulp-plumber"
notify = require "gulp-notify"

sourcemaps = (
  require("gulp-sourcemaps") if process.env.node_mode isnt "production"
)

g.task "frontend.less", ->
  pipe = g.src("./app/main.less").pipe(
    plumber "errorHandler": notify.onError '<%= error.message %>'
  )
  if process.env.node_mode isnt "production"
    pipe = pipe.pipe sourcemaps.init()
  pipe = pipe.pipe(
    less(new LessCleanCss advanced: true)
  ).pipe(
    prefixer()
  ).pipe(
    rename "assets.css"
  ).pipe(sourcemaps.write()).pipe(g.dest("./app/home/static"))
