helper = require "hyamamoto-job-toolbox/lib/helper"

module.exports =
  "basePath": "./"
  "quiet": not (helper.isProduction or process.env.node_mode is "init")
  "frameworks": ["mocha", "chai", "sinon"]
  "reporters": ["progress", "coverage"]
  "colors": true
  "logLevel": "INFO"
  "autoWatch": false
  "singleRun": helper.isProduction or process.env.node_mode is "init"
  "port": 9876
  "preprocessors":
    "app/main.coffee": ["coffee", "coverage"]
    "app/**/coffee/**/*.coffee": ["coffee", "coverage"]
    "tests/**/*.coffee": ["coffee"]
  "coffeePreprocessor":
    "options":
      "sourceMap": true
  "coverageReporter":
    "dir": "frontend_coverages"
    "type": 'lcov'
  "browsers": [
    "Chrome"
    # "Firefox"
    "PhantomJS"
  ]
  "plugins": [
    "karma-coffee-preprocessor"
    "karma-mocha"
    "karma-chai-plugins"
    "karma-chrome-launcher"
    # "karma-firefox-launcher"
    "karma-phantomjs-launcher"
    "karma-coverage"
    "karma-sinon"
  ]
