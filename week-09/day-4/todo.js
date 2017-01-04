'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var mongodb = require('mongodb');

var TodoApp = express();

var con = mongodb.MongoClient;
var collection ;

TodoApp.use(bodyParser.json());
TodoApp.use('/', express.static('./public'));

var url = 'mongodb://localhost:27017/todos';

// Use connect method to connect to the Server
con.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    console.log('Connection established to', url);

    // do some work here with the database.
    collection = db.collection('todo');
    collection.find({}).toArray(function(err, result){
      console.log(result);
    })
  }
});

TodoApp.get('/todos', function getid(req, resp) {
  collection.find({},{_id: true, text:true, completed: true}).toArray(function(err, result){
    console.log(result);
    resp.send(result);
    })
});

TodoApp.get('/todos/:id', function getid(req, resp) {
  collection.find({_id: 'ObjectId('+req.params.id+')'}).toArray(function(err, result){
    console.log(result);
    resp.send(result);
    })
});


TodoApp.post('/todos', function add(req, resp) {
  collection.insert({text: req.body.text, completed: false}, function(err, result){
    //console.log(result);
    resp.send(result);
  });
});

TodoApp.put('/todos/:id', function change(req, resp) {
  var o_id = new mongodb.ObjectID(req.params.id);
  collection.update({_id: o_id}, {$set: {completed: req.body.completed}})
  resp.send(req.params.id);
});

TodoApp.delete('/todos/:id', function del(req, resp) {
  var o_id = new mongodb.ObjectID(req.params.id);
  collection.remove({_id: o_id})
  resp.send(req.params.id);
});

//
TodoApp.listen(27017);
