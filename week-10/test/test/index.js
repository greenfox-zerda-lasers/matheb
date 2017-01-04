'use strict';

var test = require('tape');
var request = require('supertest');
var app = require('../server');

test('First test!', function (t) {
  t.end();
});

test('Playlists returned', function (t) {
  request(app)
    .get('/playlists')
    .expect('Content-Type', /json/)
    .expect(200, [
      {name: "Kicsikarcsi bal ladái"},
      {name:"All tracks"},
      {name: "Appletree"}
    ])
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();

    });
});

/*test('Playlists returned', function (t) {
  request(app)
    .get('/playlists')
    .expect('Content-Type', /json/)
    .expect(200, [
      { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
      { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
    ])
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();

    });
});*/

test('Add empty to playlists', function (t) {
  request(app)
    .post('/playlists')
    .send('vaami')
    .expect(400)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('Add correct to playlists', function (t) {
  request(app)
    .post('/playlists')
    .send({name: 'vaami'})
    .expect(200, [
      {name: "Kicsikarcsi bal ladái", id: 1},
      {name:"All tracks", id: 2},
      {name: "Appletree", id: 3},
      {name: "vaami", id: 4}
    ])
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});


test('404 on lobab', function (t) {
  request(app)
    .get('/lobab')
    .expect(404)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('teapot', function (t) {
  request(app)
    .get('/teapot')
    .expect(418)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});
