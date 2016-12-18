'use strict';

var test = require('tape');
var double = require('./39.js');

test('double numbers', function (t) {
  var actual = double(2);
  var expected = 4;

  t.equal(actual, expected);
  t.end();
});

test('input string', function (t) {
  var actual = double('alma');
  var expected = NaN;

  t.equal(actual, expected);
  t.end();
});
