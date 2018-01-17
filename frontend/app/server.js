var express = require('express');
var server = express();

server.use(express.static(__dirname));
server.use('/public', express.static(__dirname + '/public'));
server.use('/bower_components', express.static(__dirname + '/bower_components'));

server.all('/*', function(req, res, next) {
  res.sendFile('index.html', { root: __dirname });
});

var port = process.env.PORT || 8081;
server.listen(port);
console.log('Use port ' + port + ' to connect to this server');

exports = module.exports = server;
