'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortest(list){
  var short = list[0];
  for (var i = 1; i < list.length; i++){
    if (list[i].length < short.length){
      short = list[i];
    };
  };
  return short;
};

console.log(shortest(names))
