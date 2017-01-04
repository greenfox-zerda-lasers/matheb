'use strict';

var express = require('express');
var todos = require('./todos.json');
var len = todos.length + 1;
var bodyParser = require('body-parser');

var TodoApp = express();
TodoApp.use(bodyParser.json());
TodoApp.use('/', express.static('./public'));

TodoApp.get('/todos', function get(req, resp) {
  resp.send(todos);
});
