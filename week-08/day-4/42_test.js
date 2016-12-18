'use strict'

var test = require('tape');
var factor = require('./42.js');

test('3fact', function (t) {
  var actual = factor(3);
  var expected = 6;

  t.equal(actual, expected);
  t.end();
});

test('input is string', function (t) {
  t.throws(function () {
    factor('a')
  }, Error);
  t.end();
});
