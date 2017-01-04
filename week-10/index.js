'use strict';
var mysql = require("mysql");
var express = require('express');
var bodyParser = require('body-parser');

var musicPlayer = express();

musicPlayer.use(bodyParser.json());
musicPlayer.use('/', express.static('./public'));

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password:'P8r8gl1d1ng',
  database: 'musicplayer',
});

con.connect(function(err){
  if(err){
    console.log("JAAAAJ");
  } else {
  console.log("SIKERULT");
  }
});

musicPlayer.get('/playlists', function get(req, resp) {
  con.query('SELECT * FROM playlist;',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    resp.send(rows);
  });
  //resp.send(todos);
});

musicPlayer.post('/playlists', function add(req, resp) {
  con.query('INSERT INTO playlist SET ?', [{playlist: req.body.name}], function(err,res){
    if(err) throw err;
    resp.send(req.body.name);
  });
});

musicPlayer.delete('/playlist/:id', function del(req, resp) {
  con.query(
    'DELETE FROM playlist WHERE id = ?',
    [req.params.id],
    function (err, result) {
      if (err) throw err;
    }
  );
  resp.send(req.params.id);
});

musicPlayer.listen(3000, function(){
	console.log('SERVER IS UP AND RUNNIN on port: 3000')
});
