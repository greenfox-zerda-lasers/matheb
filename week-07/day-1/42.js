'use strict';

// create a function that returns it's input factorial

function factor(number){
  var counter = 1
  for (var i = 1; i <= number; i++){
    counter *= i;
  };
  return counter;
};

console.log(factor(5))
