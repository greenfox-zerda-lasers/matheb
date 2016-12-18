'use strict'

var test = require('tape');
var summa = require('./41.js');

test('sum of number', function (t) {
  var actual = summa([1, 2, 3]);
  var expected = 6;

  t.equal(actual, expected);
  t.end();
});

test('sum of words', function (t) {
  var actual = summa(['a', 'b', 'c']);
  var expected = '0abc';

  t.equal(actual, expected);
  t.end();
});

test('sum of mixture', function (t) {
  var actual = summa(['a', 3, 'c']);
  var expected = '0a3c';

  t.equal(actual, expected);
  t.end();
});
