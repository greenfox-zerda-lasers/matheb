'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function isAllPrime(arr){
  for (var i = 0; i < arr.length; i++){
    for (var j = 2; j < arr[i]; j++){
      if (arr[i] % j === 0 && arr[i] > j){
        return false;
      };
    };
  };
  return true;
};

console.log(isAllPrime(numbers));
