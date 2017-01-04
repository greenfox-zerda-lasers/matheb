var collection = [
  /* * /
  {
    title: "Demo",
    explanation: "Every week's usual stand-up.",
    src: 'img/cover.jpg'
  },
  /* */
  {
    title: "Hiking",
    explanation: "The beautiful Danube Bend from Prédikálószék.",
    src: 'img/danubeBend.jpg'
  },
  /* */
  {
    title: "Sunset",
    explanation: "Beautiful colors and icelandic horses, such and idill",
    src: 'img/sunset.jpg'
  },
  /* */
  {
    title: "Pond of Reykjavík",
    explanation: "Very nice weather at one of the last days of August 2016.",
    src: 'img/mirror.jpg'
  },
  {
    title: "Paragliding",
    explanation: "There's no better way to relax, than flying in the hills at summer.",
    src: 'img/flying.jpg'
  },
  /* */
  {
    title: "Cat",
    explanation: "Funny pet of my hosts who lived at a farm in Iceland.",
    src: 'img/cat.jpg'
  },
  {
    title: "Travelling",
    explanation: "One of the best photos I took in Iceland, near Reykjavik",
    src: 'img/travellers.jpg'
  },
  /* */
  {
    title: "Have a nice weekend",
    explanation: "It's time to enjoy the last days of the week.",
    src: 'img/rest.jpg'
  }
]


var contentList = document.querySelector(".bigPhoto");
var footer = document.querySelector(".slider");
var startPos = 0;

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
    if (i === 0){
      newThumb.setAttribute('class', 'thumb active');
    } else {
      newThumb.setAttribute('class', "thumb");
    }
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

function before_z(){
  slides[current].classList.toggle('make_z_index');
  thumbnailList[current].classList.toggle('active');
}

function after_z(){
  thumbnailList[current].classList.toggle('active');
}

function callNext(){
  if (current === slides.length-1){
    before_z();
    slides[0].classList.toggle('make_z_index');
    current = 0;
    after_z();
  } else {
  before_z();
  slides[current+1].classList.toggle('make_z_index');
  current++;
  after_z();
  }
};
next.addEventListener('click', callNext);
setTimeout(next, 3000);


var previous = document.querySelector('.previous');
function callPrevious(){
  if (current === 0){
    before_z();
    slides[slides.length-1].classList.toggle('make_z_index');
    current = slides.length-1;
    after_z();
  } else {
  before_z();
  slides[current-1].classList.toggle('make_z_index');
  current--;
  after_z();
  }
};
previous.addEventListener('click', callPrevious);
setTimeout(previous, 3000);

var thumbnailList = document.querySelectorAll('.thumb');
thumbnailList.forEach(function(item,index){
  thumbnailList[index].addEventListener('click', function(e) {
    thumbnailList[current].classList.toggle('active')
    slides[current].classList.toggle('make_z_index');
    current = parseInt(this.dataset.indexNumber);
    slides[current].classList.toggle('make_z_index');
    thumbnailList[current].classList.toggle('active')
  });
});

var menu = document.querySelectorAll('.thumb')
console.log(menu);
var thefirstChild = menu[0];
console.log(thefirstChild);

document.onkeydown = checkKey;
function checkKey(e) {
  e = e || window.event;
  // if (e.keyCode == '38') {
  //     // up arrow
  //   callPrevious();
  // }
  // else if (e.keyCode == '40') {
  //     // down arrow
  //   callNext();
  // }
  // else
  if (e.keyCode == '37') {
     // left arrow
    callPrevious();
  }
  else if (e.keyCode == '39') {
     // right arrow
    callNext();
  }
}

console.log()

var slider = document.querySelector('.slider');
var nextSlider = document.querySelector('.next_thumb');
var prevSlider = document.querySelector('.previous_thumb');
var pos = 0;

function nextPos(){
  pos -= 42;
  slider.style.left = pos + 'px';
}

nextSlider.addEventListener('click', nextPos);

function prevPos(){
  pos += 42;
  slider.style.left = pos + 'px';
}

prevSlider.addEventListener('click', prevPos);
