'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function countLetter(string){
  var letters = {};
  for (var i = 0; i < string.length; i++){
    letters[string[i]] = letters[string[i]]  + 1 || 1;
  };
  return letters;
};

console.log(countLetter('apple'));
