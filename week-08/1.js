
'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animals(sound) {
  this.sound = sound;
};

Animals.prototype.say = function(){
  console.log(this.sound);
};

var bunny = new Animals('nyuu')
bunny.say();
