'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

var filter = function filter(list){
  if (typeof list != 'object'){
    throw new Error();
  } else {
    var even = [];
    for (var i = 0; i < list.length; i++){
      if (list[i] % 2 === 0){
        even.push(list[i]);
      }
    }
  }
  return even;
};

module.exports = filter;
