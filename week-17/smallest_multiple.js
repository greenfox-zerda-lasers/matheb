// Project Euler - ID 5
// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

function multiply(array) {
  var current = 1;
  for (var i = 0; i < array.length; i++) {
    current *= array[i];
  }
  return current;
}

function findPrimes(number) {
  var i = 2;
  var primes = [];
  while ( number != 1 ) {
    if ( number % i != 0) {
      i++;
    } else {
      primes.push(i);
      number /= i;
    }
  }
  return primes;
}

function smallestMultiple(number) {
  var array = [1];
  for ( var i = 1; i < number+1; i++) {
    // console.log(i)
    if ( multiply(array) % i != 0) {
      var primes = findPrimes(i);
      // console.log(primes)
      for (var j = 0; j < primes.length; j++) {
        if (!array.slice(primes[j-1], primes.length).includes(primes[j])){
          array.push(primes[j]);
          console.log(array, i,': ',primes)
        }
      }
    }
  }
  return multiply(array);
}



console.log(multiply([1,2,3,4]));

console.log(smallestMultiple(20));

console.log(findPrimes(24))
