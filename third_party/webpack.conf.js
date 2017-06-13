((require) => {
  const path = require('path');
  const pathHere = path.resolve(__dirname);

  const packageTemplate = require('../webpack.conf.js');
  module.exports = packageTemplate({
    third_party: path.join(pathHere, 'main.js'),
  }, pathHere, '../app/common/static');
  module.exports.resolve = {
    modules: [path.join(pathHere, 'bower_components')],
  };
})(require);
