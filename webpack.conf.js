((require) => {
  const path = require('path');

  const webpack = require('webpack');

  const Uglify = require('uglifyjs-webpack-plugin');
  const ExtractTextPlugin = require('extract-text-webpack-plugin');

  const toolbox = require('hyamamoto-job-toolbox');
  const isProd = toolbox.helper.isProduction;

  module.exports = (entry, modulePath, outpath = 'static') => ({
    entry,
    output: {
      path: path.resolve(path.join(modulePath, outpath)),
      filename: '[name].js',
    },
    plugins: [
      new webpack.SourceMapDevToolPlugin(),
      new Uglify({ sourceMap: !isProd }),
      new ExtractTextPlugin('[name].css'),
    ],
    target: 'web',
    module: require('./module_rulse.js'),
  });
})(require);
