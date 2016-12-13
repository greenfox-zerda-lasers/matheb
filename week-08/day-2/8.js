'use strict'

// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false] with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
//  - tour should return the result of walk

var arr = [];

function tour(){
  walk(3);
  console.log(distance());
};

function walk(steps){
  for (var i = 0; i < steps; i++){
    arr.push('false');
    console.log(arr);
  }
};

function distance(){
  for (var i = 0; i < arr.length; i++){
    arr[i] = 'true';
  }
  return arr;
};

tour();
