'use strict';

var express = require('express');

var exampleApp = express();

exampleApp.get('/', function get(req, resp) {
  resp.send('Hello bello');
});

exampleApp.post('/', function send(req, resp) {
  resp.send('Postoltal');
});

exampleApp.listen(3000);
