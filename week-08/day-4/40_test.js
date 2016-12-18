'use strict'

var test = require('tape');
var writeA = require('./40.js');

test('write a to end', function (t) {
  var actual = writeA('kuty');
  var expected = 'kutya';

  t.equal(actual, expected);
  t.end();
});

test('input is number', function (t) {
  var actual = writeA(3);
  var expected = 3+"a";

  t.equal(actual, expected);
  t.end();
});

test('input is list', function (t) {
  var actual = writeA([1, 2, 3]);
  var expected = [1, 2, 3]+"a";

  t.equal(actual, expected);
  t.end();
});
