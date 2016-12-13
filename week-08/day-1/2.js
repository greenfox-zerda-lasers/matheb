'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(a, b){
  this.a = a;
  this.b = b;
};

Rectangles.prototype.getArea = function(){
  this.area = this.a * this.b;
  console.log(this.area);
};

Rectangles.prototype.getCircumference = function(){
  this.circumference = 2 * ( this.a + this.b );
  console.log(this.circumference);
};

var rect1 = new Rectangles(2, 3);
rect1.getArea();
rect1.getCircumference();
