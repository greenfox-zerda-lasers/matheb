'use strict';

var k = 1521;
// tell if k is dividable by 3 or 5
if (k%3 === 0 && k%5 === 0){
  console.log(k+" is dividable by 3 and 5")
} else if (k%3 === 0){
  console.log(k+" is dividable by 3")
} else if (k%5 === 0){
  console.log(k+" is dividable by 5")
} else {
  console.log(k+" is not dividable by 3 or 5")
}
