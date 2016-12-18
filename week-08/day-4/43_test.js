'use strict'

var test = require('tape');
var filter = require('./43.js');

test('3fact', function (t) {
  var actual = filter([1, 2, 3, 4, 6]);
  var expected = [2, 4, 6];

  t.equal(actual, expected);
  t.end();
});

test('input not list', function (t) {
  t.throws(function(){
    filter(1)
  }, Error);
  t.end();
});
