'use strict';

var numbers = [2.4, 3.5, 1.7, 3.3, 1.2];

// create a function that takes an array of numbers,
// it should return a new array that consists only the numbers that are
// bigger than 2 and all of it's elements should be rounded

function filterBigger(arr){
  var newArr = [];
  arr.forEach(function(item,index){
    if (Math.round(item) > 2){
      newArr.push(Math.round(item));
    };
  });
  return newArr;
};

console.log(filterBigger(numbers));

/* * /
function filterBigger2(arr){
  var newArr = [];
  if (arr.length > 0) {
    if (Math.round(arr[0]) > 2){
      newArr.push(Math.round(arr[0]));
      arr.shift();
    };
    filterBigger2(arr);
  };
  return newArr;
};

console.log(filterBigger2(numbers));
/* */
