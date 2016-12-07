'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack() {
  this.arr = [];
  this.size = function(){
    var counter = 0;
    this.arr.forEach(function(item,index){
	    counter += 1;
    });
    return counter;
  },
  this.push = function(number){
    this.arr[this.size()] = number;
    return this.arr;
  },
  this.pop = function(){
    console.log(this.arr[this.size()-1]);
    this.arr = this.arr[0, this.size()-2];
    return this.arr;
  };
};

var stack = new Stack();

console.log(stack.size());
console.log(stack.push(4));
console.log(stack.push(5));
console.log(stack.pop());
console.log(stack);
