((require) => {
  const path = require('path');

  const webpack = require('webpack');

  const ExtractTextPlugin = require('extract-text-webpack-plugin');
  const toolbox = require('hyamamoto-job-toolbox');

  module.exports = (entry, modulePath, outpath = 'static') => ({
    mode: (toolbox.helper.isProduction) ? 'production' : 'development',
    entry,
    output: {
      path: path.resolve(path.join(modulePath, outpath)),
      filename: '[name].js',
    },
    plugins: [
      new ExtractTextPlugin('[name].css'),
    ],
    target: 'web',
    module: require('./module_rules.js'),
  });
})(require);
