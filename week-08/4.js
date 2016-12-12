// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

function airCrafts(type){
  this.type = type;
  this.maxAmmo = 0;
  this.ammo = 0;
  this.baseDamage = 0;
  this.allDamage = 0;
  this.necessaryAmmo = 0;
};

airCrafts.prototype.setDetails = function(){
  if (this.type === 'F16'){
    this.maxAmmo = 8;
    this.baseDamage = 30;
    this.allDamage = this.baseDamage;
    console.log('Type: '+this.type+ ' Ammo: '+this.ammo+' baseDamage: '+this.baseDamage);
  } else if (this.type === 'F35'){
    this.maxAmmo = 12;
    this.baseDamage = 50;
    this.allDamage = this.baseDamage;
    console.log('Type: '+this.type+ ' Ammo: '+this.ammo+' baseDamage: '+this.baseDamage);
  }
};

airCrafts.prototype.fight = function(){
  this.baseDamage = this.ammo * this.baseDamage;
  this.ammo = 0;
};

airCrafts.prototype.refill = function(ammo){
  if (this.maxAmmo < this.ammo + ammo){
    this.ammo = this.maxAmmo;
    this.necessaryAmmo = (this.ammo + ammo)-this.maxAmmo;
  } else {
    this.ammo += ammo;
    this.necessaryAmmo = (this.ammo + ammo)-this.maxAmmo;
  }
};

function Carrier(){
  this.list = [];
  this.allDamage = 0;
  this.healthPoints = 3000;
  this.ammoStorage = 2300;
};

Carrier.prototype.storeAircrafts = function(airCraft){
  this.list.push(airCraft);
  this.allDamage += airCraft.allDamage;
  this.ammoStorage -= airCraft.ammo;
  console.log('Type: '+airCraft.type+ ' Ammo: '+airCraft.ammo+' Base Damage: '+airCraft.baseDamage+' All Damage: '+this.allDamage);
};

Carrier.prototype.statusReport = function(){
  if (this.healthPoints > 0){
    console.log('Aircraft count: '+this.list.length+', Ammo Storage: '+this.ammoStorage+ ', Total damage: '+this.allDamage+', Health Remaining: '+(this.healthPoints-this.allDamage)+'\nAircrafts');
    for (var i = 0; i < this.list.length; i++){
      console.log('Type: '+this.list[i]['type']+', Ammo: '+this.list[i]['ammo']+', Base Damage: '+this.list[i]['allDamage']+', All Damage: '+this.list[i].baseDamage);
    }
  } else {
    console.log("It's dead Jim :(.");
  }
};

Carrier.prototype.add_aircraft = function(aircraft, type){
  var aircraft = new airCrafts(type);
  aircraft.setDetails();
  carrier.storeAircrafts(aircraft);
};

Carrier.prototype.fill = function(ammo){
  if (this.ammoStorage-(this.list.length*ammo) < 0){
    console.log("You don't have enough ammo.");
  } else {
    for (var i = 0; i < this.list.length; i++){
      this.list[i].refill(ammo);
      this.ammoStorage -= this.list[i]['necessaryAmmo'];
    }
  }
};

Carrier.prototype.fight = function(){
  var all_damage = 0;
  for (var i = 0; i < this.list.length; i++){
    all_damage += this.list[i]['ammo']*this.list[i]['baseDamage'];
    this.list[i]['baseDamage'] *= this.list[i]['ammo'];
    this.list[i]['ammo'] = 0;
  };
  this.allDamage = all_damage;
};

var air1 = new airCrafts('F16');
var air2 = new airCrafts('F35');
air1.setDetails();
air2.setDetails();
air1.refill(5);
var carrier = new Carrier;
carrier.storeAircrafts(air1);
carrier.storeAircrafts(air2);
carrier.statusReport();
carrier.fill(10);
carrier.statusReport();
carrier.fight();
carrier.statusReport();
