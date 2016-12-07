'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

function sayNumber(number){
  number = Math.abs(number);
  switch (number) {
    case 0:
      return 'Zero';
      break;
    case 1:
      return 'One';
      break;
    case 2:
      return 'Two';
      break;
    case 3:
      return 'Three';
      break;
    case 4:
      return 'Four';
      break;
    case 5:
      return 'Five';
      break;
    default:
      return 'Many';
      break;
  };
};

console.log(sayNumber(-1))
