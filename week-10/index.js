'use strict';
var mysql = require("mysql");
var express = require('express');
var bodyParser = require('body-parser');
var cors = require('cors')

var musicPlayer = express();
musicPlayer.use(cors());

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
});

musicPlayer.get('/playlists/:id', function getid(req, resp) {
  var num = req.params.id;
  con.query('SELECT * FROM playlist WHERE id = ?;', [num], function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    resp.send(rows);
  });
});

musicPlayer.post('/playlists', function add(req, resp) {
  con.query('INSERT INTO playlist SET ?', [{playlist: req.body.name}], function(err,res){
    if(err) throw err;
    con.query('SELECT * FROM playlist', function(req, rows){
      if(err) throw err;
      resp.send(rows);
    });
  });
});

musicPlayer.delete('/playlists/:id', function del(req, resp) {
  console.log(req.params.id)
  con.query('DELETE FROM playlist WHERE id = ?', [req.params.id], function (err, result) {
    if (err) throw err;
    con.query('SELECT * FROM playlist', function(req, rows){
      if(err) throw err;
      resp.send(rows);
    });
  });
});

musicPlayer.get('/playlist-tracks', function get(req, resp) {
  con.query('SELECT * FROM tracks;',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    resp.send(rows);
  });
});

musicPlayer.get('/playlist-tracks/:playlist_id', function get(req, resp) {
  con.query('SELECT * FROM tracks WHERE playlist_id = ?', [req.params.playlist_id],function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    resp.send(rows);
  });
});

musicPlayer.post('/playlist-tracks/:playlist_id', function add(req, resp) {
  con.query('INSERT INTO tracks SET ?', [{playlist_id: req.params.playlist_id}], function(err,res){
    if(err) throw err;
    con.query('SELECT * FROM tracks', function(req, rows){
      if(err) throw err;
      resp.send(rows);
    });
  });
});

musicPlayer.listen(3000, function(){
	console.log('SERVER IS UP AND RUNNIN on port: 3000')
});
