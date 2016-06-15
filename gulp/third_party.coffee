g = require "gulp"
plumber = require "gulp-plumber"
notify = require "gulp-notify"
uglify = require "gulp-uglify"
concat = require "gulp-concat"
srcmap = require "gulp-sourcemaps"

thirdPartyPrefix = "./app/static"
module.exports =
  "thirdPartyPackages": [
    "#{thirdPartyPrefix}/modernizr.js"
    "#{thirdPartyPrefix}/detectizr/dist/detectizr.js"
    "#{thirdPartyPrefix}/jquery/dist/jquery.js"
    "#{thirdPartyPrefix}/bootstrap/dist/js/bootstrap.js"
    "#{thirdPartyPrefix}/angular/angular.js"
    "#{thirdPartyPrefix}/angular-animate/angular-animate.js"
    "#{thirdPartyPrefix}/angular-resource/angular-resource.js"
    "#{thirdPartyPrefix}/angular-ui-router/release/angular-ui-router.js"
    "#{thirdPartyPrefix}/AngularJS-Toaster/toaster.js"
  ]
  "thirdPartyPrefix": thirdPartyPrefix

g.task "third_party", ->
  thirdPartyPackages = module.exports.thirdPartyPackages
  if process.env.node_mode isnt "production"
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
