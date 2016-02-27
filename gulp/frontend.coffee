g = require "gulp"
plumber = require "gulp-plumber"
notify = require "gulp-notify"
rename = require "gulp-rename"
concat = require "gulp-concat"

prefixer = require "gulp-autoprefixer"
less = require "gulp-less"
LessCleanCss = require "less-plugin-clean-css"

coffee = require "gulp-coffee"
coffeelint = require "gulp-coffeelint"
uglify = require "gulp-uglify"

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
    less(
      "plugins": [
        new LessCleanCss(advanced: true)
      ]
    )
  ).pipe(
    prefixer()
  ).pipe(
    rename "assets.css"
  )
  if process.env.node_mode isnt "production"
    pipe = pipe.pipe(sourcemaps.write())
  pipe.pipe(g.dest("./app/home/assets"))


g.task "frontend.coffee", ->
  pipe = g.src([
    "./app/**/coffee/**/*.coffee"
    "./app/main.coffee"
  ]).pipe plumber "errorHandler": notify.onError '<%= error.message %>'

  if process.env.node_mode isnt "production"
    pipe = pipe.pipe(sourcemaps.init())
  pipe = pipe.pipe(
    coffeelint "./coffeelint.json"
  ).pipe(
    coffeelint.reporter "coffeelint-stylish"
  ).pipe(
    coffeelint.reporter "failOnWarning"
  ).pipe(
    coffee()
  ).pipe(
    concat "assets.js"
  ).pipe(uglify "mangle": true)
  if process.env.node_mode isnt "production"
    pipe = pipe.pipe(sourcemaps.write())
  pipe.pipe g.dest "./app/home/assets"
