'use strict'

function binSearch(array, number){
  array.sort();

  var min = 0;
  var max = array.length - 1;
  var guess;

  while(min <= max) {
    guess = Math.floor((max + min) / 2);

    if (array[guess] === number) {
      return true;
    }
    else if (array[guess] < number) {
      min = guess + 1;
    }
    else {
      max = guess - 1;
    }

  }

  return false;

};

console.log(binSearch([1,2,3,4,5], 6));
