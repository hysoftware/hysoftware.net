g = require "gulp"
plumber = require "gulp-plumber"
notify = require "gulp-notify"
uglify = require "gulp-uglify"
concat = require "gulp-concat"
srcmap = require "gulp-sourcemaps"

thirdPartyPrefix = exports.thirdPartyPrefix = "./app/static"

g.task "third_party", ->
  thirdPartyPackages = [
    "#{thirdPartyPrefix}/jquery/dist/jquery.js"
    "#{thirdPartyPrefix}/modernizr.js"
    "#{thirdPartyPrefix}/detectizr/dist/detectizr.js"
    "#{thirdPartyPrefix}/bootstrap/dist/js/bootstrap.js"
    "#{thirdPartyPrefix}/angular/angular.js"
    "#{thirdPartyPrefix}/angular-resource/angular-resource.js"
    "#{thirdPartyPrefix}/angular-ui-router/release/angular-ui-router.js"
  ]
  if process.env.mode isnt "production"
    thirdPartyPackages.splice(
      thirdPartyPackages.indexOf(
        "#{thirdPartyPrefix}/angular/angular.js"
      ) + 1, 0, "#{thirdPartyPrefix}/angular-mocks/angular-mocks.js"
    )
  g.src(thirdPartyPackages).pipe(
    plumber "errorHandler": notify.onError '<%= error.message %>'
  ).pipe(
    srcmap.init()
  ).pipe(concat "third_party.js").pipe(
    uglify "mangle": false
  ).pipe(
    srcmap.write()
  ).pipe g.dest thirdPartyPrefix
