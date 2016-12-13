var candies = 0;
var lollypops = 0;
var rate = 0;
var speed = 1000;
//🍭

var showCandies = document.querySelector('.candies');
var showLollys = document.querySelector('.lollypops');
var showRate = document.querySelector('.speed');

var createButton = document.querySelector(".create-candies");
var buyButton = document.querySelector(".buy-lollypops");
var rainButton = document.querySelector(".candy-machine");

function addCandy(){
  candies += 1;
  showCandies.textContent = candies;
};
createButton.addEventListener('click', addCandy);

function buyLolly(){
  if (candies >= 10){
    candies -= 10;
    lollypops += 1;
    console.log(lollypops+' '+candies);
    var lolly = document.createElement('div');
    lolly.style.display = 'inline-block';
    lolly.textContent = '🍭';
    showLollys.appendChild(lolly);
    showCandies.textContent = candies;
  }
};
createButton.addEventListener('click', addCandy);
buyButton.addEventListener('click', buyLolly);

function rain(){
  speed /= 10;
}
rainButton.addEventListener('click', rain);

function generateCandy(){
  candies += Math.floor(lollypops/10);
  showCandies.textContent = candies;
  rate = Math.floor(lollypops/10)*(1000/speed);
  showRate.textContent = rate;
  setTimeout(generateCandy, speed);
};
setTimeout(generateCandy, speed);
