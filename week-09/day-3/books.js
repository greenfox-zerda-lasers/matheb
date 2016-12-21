'use strict';

var mysql = require("mysql");
var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());
TodoApp.use('/', express.static('./public'));

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password:'alma',
  database: 'bookstore',
});

con.connect(function(err){
  if(err){
    console.log("JAAAAJ");
  } else {
  console.log("SIKERULT");
  }
});

// app.get('/', function(req, res) {
//   con.query('SELECT book_name FROM book_mast;',function(err,rows){
//     if(err) {
//       console.log(err.toString());
//       return;
//     }
//     res.send(rows);
//   });
// });

app.get('/', function(req, res) {
  con.query("SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast \
  INNER JOIN author ON book_mast.aut_id = author.aut_id \
  INNER JOIN category ON book_mast.cate_id = category.cate_id \
  INNER JOIN publisher ON book_mast.pub_id = publisher.pub_id;",function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(rows);
  });
});

app.listen(3000);
