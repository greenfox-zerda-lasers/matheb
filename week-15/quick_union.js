function quickUnion(arrayLength) {
  this.array = [];
  this.length = arrayLength;
  for ( var i = 1; i < this.length; i++) {
    this.array.push(i);
  }
};
//
quickUnion.prototype.unite = function(a, b) {
  if (a < this.length && b < this.length){
    this.array[a] = b;
  } else {
    console.log('please add valid indexes');
  }
};

quickUnion.prototype.find = function(a, b) {
  if (a < this.length && b < this.length){
    if ( this.array[a-1] === this.array[b]){
      return true;
    } else {
      return false;
    }
  } else {
    console.log('please add valid indexes');
  }
};

quickUnion.prototype.getGroups = function() {
  var groups = [];
  array = this.array;
  array.forEach(function(groupID){
    if(!groups.includes(groupID)){
      groups.push(groupID);
    }
  })
  return groups;
}

var myarray = new quickUnion(9);
myarray.unite(8,1);
console.log(myarray);
// myarray.unite(5,2);
// console.log(myarray);
// myarray.unite(6,3);
// console.log(myarray);
// myarray.unite(8,1);
// console.log(myarray);
console.log("groups",myarray.getGroups());
// 01678
// 2
// 3
// 4
// 5

console.log(myarray.find(2,3));
