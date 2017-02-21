// Project Euler - ID 4:
// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two 3-digit numbers.

function findLargestPalindrom() {
  var a;
  var palindrom = [];
  for (var i = 999; i >= 100; i--){
    for ( var j = 999; j >= 100; j--){
      a = i*j;
      var aa = a.toString();
      var b = aa.split("").reverse().join("");
      var d = Number(b);
      if ( a - d === 0 ) {
        palindrom.push(a);
      }
    }
  }
  return Math.max.apply(Math, palindrom);
}

console.log(findLargestPalindrom());
