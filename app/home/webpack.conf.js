((require) => {
  const path = require('path');
  const pathHere = path.resolve(__dirname);

  const packageTemplate = require('../../webpack.conf.js');
  module.exports = packageTemplate({
    home: path.join(pathHere, 'main.js'),
  }, pathHere, 'jinja2');
})(require);
