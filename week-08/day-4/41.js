'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

var sum = function summa(numbers){
  var counter = 0
  for (var i = 0; i < numbers.length; i++){
    counter += numbers[i];
  };
  return counter;
};

module.exports = sum;
