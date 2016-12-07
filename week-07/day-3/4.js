'use strict';

var af = [4, 5, 6, 7];
// print all the elements of af, dont use for or while :)

af.forEach(function(item,index){
	console.log(item);
});

function second(arr){
  if (arr.length > 0){
    console.log(arr[0]);
    arr.shift();
    second(arr);
  };
};

second(af);
