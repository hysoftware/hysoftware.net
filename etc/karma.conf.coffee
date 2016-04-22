helper = require "hyamamoto-job-toolbox/lib/helper"

module.exports =
    "basePath": "./"
    "quiet": not (helper.isProduction or process.env.node_mode is "init")
    "frameworks": ["mocha", "chai", "sinon"]
    "reporters": ["progress"]
    "colors": true
    "logLevel": "INFO"
    "autoWatch": false
    "singleRun": helper.isProduction or process.env.node_mode is "init"
    "port": 9876
    "preprocessors":
      "**/*.coffee": ["coffee"]
    "coffeePreprocessor":
      "options":
        "sourceMap": true
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
      "karma-sinon"
    ]
