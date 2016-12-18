'use strict';

// create a function that returns it's input factorial

var fact = function factor(number){
  var counter = 1
  if (typeof number != 'number'){
    throw new Error();
  } else {
    for (var i = 1; i <= number; i++){
      counter *= i;
    }
  }
  return counter;
};

module.exports = fact;
