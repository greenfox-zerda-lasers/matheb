'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rockets(neededFuel){
  this.neededFuel = neededFuel;
  this.fuel = 0;
  this.fuelMax = 30;
};

Rockets.prototype.fill = function(amount){
  //console.log(amount);
  if (this.fuelMax < this.fuel + amount){
    console.log(this.fuel);
    this.fuel = this.fuelMax;
    console.log(this.fuel);
  } else {
    this.fuel += amount;
    console.log(this.fuel);
  }
};

Rockets.prototype.launch = function(){
  if (this.fuel >= this.neededFuel){
    console.log('Launch');
  };
};

var rocket1 = new Rockets(10);
rocket1.fill(5);
rocket1.launch();
rocket1.fill(6);
rocket1.launch();
rocket1.fill(20);
