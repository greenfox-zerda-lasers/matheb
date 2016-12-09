var collection = [
  {
    title: "Pond of Reykjavik",
    explanation: "Wonderful weather at one of the last days of August 2016",
    src: 'img/mirror.jpg'
  },
  {
    title: "Paragliding at summer",
    explanation: "There's no better way to relax, than flying in the hills at summer.",
    src: 'img/flying.jpg'
  },
  {
    title: "Have a nice weekend",
    explanation: "It's time to enjoy the last days of the week.",
    src: 'img/rest.jpg'
  }
]

var contentList = document.querySelector(".bigPhoto");
var footer = document.querySelector(".pics");

function fillContent(){

  for (var i = 0; i < collection.length; i++){
    var newSlide = document.createElement('div');
    newSlide.setAttribute('class', 'slide');
    if (i === 0){
      newSlide.setAttribute('class', 'slide make_z_index');
    };

    var newImage = document.createElement('img');
    newImage.setAttribute('src', collection[i]['src']);
    newSlide.appendChild(newImage);

    var newThumb = document.createElement('img');
    newThumb.setAttribute('src', collection[i]['src']);
    newThumb.setAttribute('class', "thumb");
    newThumb.setAttribute('data-index-Number', i);
    if (i === 0){
      newSlide.setAttribute('class', 'slide make_z_index');
    };
    footer.appendChild(newThumb);

    var exp = document.createElement('section');
    exp.setAttribute('class', 'current');

    var newTitle = document.createElement('h1');
    newTitle.textContent = collection[i]['title'];
    exp.appendChild(newTitle);

    var newPar = document.createElement('p');
    newPar.textContent = collection[i]['explanation'];
    exp.appendChild(newPar);

    newSlide.appendChild(exp);
    contentList.appendChild(newSlide);
  };
};

fillContent();
var current = 0;
var slides = document.querySelectorAll('.slide');

var next = document.querySelector('.next');
function callNext(){
  if (current === slides.length-1){
    slides[current].classList.toggle('make_z_index');
    thumbnailList[current].style.opacity = 0.6;
    slides[0].classList.toggle('make_z_index');
    current = 0;
    thumbnailList[current].style.opacity = 1;
  } else {
  slides[current].classList.toggle('make_z_index');
  thumbnailList[current].style.opacity = 0.6;
  slides[current+1].classList.toggle('make_z_index');
  current++;
  thumbnailList[current].style.opacity = 1;
  }
};
next.addEventListener('click', callNext);


var previous = document.querySelector('.previous');
function callPrevious(){
  if (current === 0){
    slides[current].classList.toggle('make_z_index');
    thumbnailList[current].style.opacity = 0.6;
    slides[slides.length-1].classList.toggle('make_z_index');
    current = slides.length-1;
    thumbnailList[current].style.opacity = 1;
  } else {
  slides[current].classList.toggle('make_z_index');
  thumbnailList[current].style.opacity = 0.6;
  slides[current-1].classList.toggle('make_z_index');
  current--;
  thumbnailList[current].style.opacity = 1;
  }
};
previous.addEventListener('click', callPrevious);

var thumbnailList = document.querySelectorAll('.thumb');
thumbnailList.forEach(function(item,index){
  thumbnailList[index].addEventListener('click', function(e) {
    thumbnailList[current].style.opacity = 0.6;
  	this.style.opacity = 1;
    slides[current].classList.toggle('make_z_index');
    current = parseInt(this.dataset.indexNumber);
    slides[current].classList.toggle('make_z_index');
  });
});
