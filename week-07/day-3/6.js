'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function consist(string, letter){
  if (string.indexOf(letter) >= 0){
    return true;
  } else {
    return false;
  };
};

console.log(consist('alma', 'a'));
console.log(consist('alma', 'k'));
