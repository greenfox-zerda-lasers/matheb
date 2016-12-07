'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  sum : 0,
  grades : [],
  addgrade : function(grade){
    this.grades.push(grade);
    return this.sum += grade;
  },
  getAverage : function(sum, grades){
    return sum/grades.length;
  }
};

console.log(student.addgrade(5));
console.log(student.addgrade(1));
console.log(student.addgrade(2));
console.log(student.getAverage(student.sum, student.grades));
