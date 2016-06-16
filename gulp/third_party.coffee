g = require "gulp"
plumber = require "gulp-plumber"
notify = require "gulp-notify"
uglify = require "gulp-uglify"
concat = require "gulp-concat"
srcmap = require "gulp-sourcemaps"
toolboxHelper = require "hyamamoto-job-toolbox/lib/helper"

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
  pipe = g.src(thirdPartyPackages).pipe(
    plumber "errorHandler": notify.onError '<%= error.message %>'
  )
  if not toolboxHelper.isProduction
    pipe = pipe.pipe(
      srcmap.init()
    )
  pipe = pipe.pipe(concat "third_party.js").pipe(
    uglify "mangle": false
  )
  if not toolboxHelper.isProduction
    pipe = pipe.pipe(
      srcmap.write()
    )
  pipe.pipe g.dest thirdPartyPrefix
