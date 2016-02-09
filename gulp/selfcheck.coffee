g = require "gulp"
plumber = require "gulp-plumber"
notify = require "gulp-notify"
lint = require "gulp-coffeelint"

g.task "selfcheck", ->
  g.src([
      "./gulpfile.coffee",
      "./gulp/**/*.coffee"
  ]).pipe(
    plumber "errorHandler": notify.onError '<%= error.message %>'
  ).pipe(
    lint "./coffeelint.json"
  ).pipe(
    lint.reporter "coffeelint-stylish"
  ).pipe(
    lint.reporter "failOnWarning"
  )
