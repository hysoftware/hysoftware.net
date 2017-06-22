((require) => {
  const path = require('path');

  const webpack = require('webpack');

  const ExtractTextPlugin = require('extract-text-webpack-plugin');
  const Babili = require('babili-webpack-plugin');
  const toolbox = require('hyamamoto-job-toolbox');

  module.exports = (entry, modulePath, outpath = 'static') => ({
    entry,
    output: {
      path: path.resolve(path.join(modulePath, outpath)),
      filename: '[name].js',
    },
    plugins: [
      new webpack.SourceMapDevToolPlugin(),
      new Babili({}, { sourceMap: !toolbox.helper.isProduction }),
      new ExtractTextPlugin('[name].css'),
    ],
    target: 'web',
    module: require('./module_rules.js'),
  });
})(require);
