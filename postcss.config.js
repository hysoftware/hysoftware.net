((require) => {
  const toolbox = require('hyamamoto-job-toolbox');
  module.exports = {
    plugins: [
      require('postcss-clean')({ sourceMap: !toolbox.helper.isProduction }),
      require('autoprefixer')(),
    ],
  };
})(require);
