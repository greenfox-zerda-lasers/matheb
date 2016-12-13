var candies = 0;
var lollypops = 0;
var rate = 0;
//🍭

var showCandies = document.querySelector('.candies');
var showLollys = document.querySelector('.lollypops');
var showRate = document.querySelector('.speed');

var createButton = document.querySelector(".create-candies");
var buyButton = document.querySelector(".buy-lollypops");

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

function generateCandy(){
  candies += Math.floor(lollypops/10);
  showCandies.textContent = candies;
  rate = Math.floor(lollypops/10);
  showRate.textContent = rate;
  setTimeout(generateCandy, 1000);
};
setTimeout(generateCandy, 1000);
