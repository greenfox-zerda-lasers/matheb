function quickUnion(arrayLength) {
  this.array = [];
  this.length = arrayLength;
  for ( var i = 1; i < this.length+1; i++) {
    this.array.push(i);
  }
  //console.log(this.array)
};
//

quickUnion.prototype.root = function(index){
  //console.log(this.array[index])
  while (index != this.array[index-1]){
    index = this.array[index-1];
  }
  return index;
};


quickUnion.prototype.unite = function(a, b) {
  if (!this.find(a,b)){
    this.array[a-1] = b;
    return this.array;
  } else {
    console.log('Already connected');
  }
};

quickUnion.prototype.find = function(a, b) {
  if (a < this.length && b < this.length){
    console.log(this.root(a));
    console.log(this.root(b));
    if ( this.root(a) === this.root(b)){
      return true;
    } else {
      return false;
    }
  } else {
    console.log('please add valid indexes');
  }
};

quickUnion.prototype.getGroups = function(){
  var groups = [];
  array = this.array;
  for ( var i = 0; i < array.length; i++){
    groups.push(this.root(array[i]));
  };
  return groups.sort();
}

var myarray = new quickUnion(9);
//console.log(myarray.root(3));
//console.log(myarray.find(2,3));
console.log(myarray.unite(8,1));
console.log(myarray.unite(1,2));
console.log(myarray.unite(1,8));

console.log(myarray.getGroups());
