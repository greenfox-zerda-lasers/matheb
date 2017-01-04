'use strict';

var express = require('express');
var app = express();
var playlists = [
  {name: "Kicsikarcsi bal ladái", id: 1},
  {name:"All tracks", id: 2},
  {name: "Appletree", id: 3}
]

var idCount = 3;

var playlist_tracks = [
  { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
  { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
]

app.get('/playlists', function (req, res) {
  res.send(playlists);
});

app.post('/playlists', function (req, res) {
  if(typeof req.body !== "object"){
    res.sendStatus(400);
  } else if(!req.body.hasOwnProperty("name")){
    res.sendStatus(400)
  } else {
    idCount += 1;
    playlists.push({name: req.body.name, id: idCount});
    res.send(playlist);
  }
});

app.get('/teapot', function (req, res) {
  res.sendStatus(418);
});

module.exports = app;
