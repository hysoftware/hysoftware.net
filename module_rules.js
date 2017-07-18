((require) => {
  const toolbox = require('hyamamoto-job-toolbox');
  const ExtractTextPlugin = require('extract-text-webpack-plugin');
  const isProd = toolbox.helper.isProduction;
  module.exports = {
    rules: [
      {
        test: /\.es6$/,
        use: [{
          loader: 'babel-loader',
          options: {
            presets: ['env'],
          },
        }],
      }, {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract({
          fallback: {
            loader: 'style-loader', options: { sourceMap: !isProd },
          },
          use: [
            {
              loader: 'css-loader',
              options: { sourceMap: !isProd, importLoaders: 2 },
            },
            { loader: 'postcss-loader', options: { sourceMap: !isProd } },
            { loader: 'sass-loader', options: { sourceMap: !isProd } },
          ],
        }),
      }, {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
          fallback: {
            loader: 'style-loader', options: { sourceMap: !isProd },
          },
          use: [
            {
              loader: 'css-loader',
              options: { sourceMap: !isProd, importLoaders: 1 },
            },
            { loader: 'postcss-loader', options: { sourceMap: !isProd } },
          ],
        }),
      },
      {
        test: /\.(?:woff|eot|ttf|svg|jpg|png)/,
        use: [{ loader: 'url-loader' }],
      },
    ],
  };
})(require);
