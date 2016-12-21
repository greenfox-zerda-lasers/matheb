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

TodoApp.get('/todos/:id', function getid(req, resp) {
  resp.send(todos[parseInt(req.params.id - 1)]);
});

TodoApp.post('/todos', function add(req, resp) {
  console.log(req.body);
  todos.push({ id: todos[todos.length - 1].id + 1, text: req.body.text, completed: false });
  resp.send(todos);
});

TodoApp.put('/todos/:id', function change(req, resp) {
  var putId = parseInt(req.params.id);

  todos.forEach(function(item){
    if(item.id === putId){
      item.completed = !item.completed;
    }
  });

  //todos[req.params.id - 1] = ({ completed: !todos[req.params.id - 1].completed, id: parseInt(req.params.id), text: req.body.text });
  resp.send(todos);
});

TodoApp.delete('/todos/:id', function del(req, resp) {
  //todos[req.params.id - 1] = null; //({ completed: false, id: parseInt(req.params.id), text: todos[req.params.id - 1].text, destroyed: true });
  var deleteId = parseInt(req.params.id);

  function rightId(todoListElem) {
    return todoListElem.id !== deleteId;
  }

  todos = todos.filter(rightId);

//console.log(todoList);
  resp.send(todos);
});


TodoApp.listen(3000);
