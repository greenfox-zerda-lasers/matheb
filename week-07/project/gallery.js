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
    thumbnailList[current+1].style.opacity = 0.4;
    thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,0)";
    slides[0].classList.toggle('make_z_index');
    current = 0;
    thumbnailList[current+1].style.opacity = 1;
    thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,1)";
  } else {
  slides[current].classList.toggle('make_z_index');
  thumbnailList[current+1].style.opacity = 0.4;
  thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,0)";
  slides[current+1].classList.toggle('make_z_index');
  current++;
  thumbnailList[current+1].style.opacity = 1;
  thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,1)";
  }
};
next.addEventListener('click', callNext);


var previous = document.querySelector('.previous');
function callPrevious(){
  if (current === 0){
    slides[current].classList.toggle('make_z_index');
    thumbnailList[current+1].style.opacity = 0.4;
    thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,0)";
    slides[slides.length-1].classList.toggle('make_z_index');
    current = slides.length-1;
    thumbnailList[current+1].style.opacity = 1;
    thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,1)";
  } else {
  slides[current].classList.toggle('make_z_index');
  thumbnailList[current+1].style.opacity = 0.4;
  thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,0)";
  slides[current-1].classList.toggle('make_z_index');
  current--;
  thumbnailList[current+1].style.opacity = 1;
  thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,1)";
  }
};
previous.addEventListener('click', callPrevious);

var thumbnailList = document.querySelectorAll('.thumb');
thumbnailList.forEach(function(item,index){
  thumbnailList[index].addEventListener('click', function(e) {
    thumbnailList[current+1].style.opacity = 0.4;
    thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,0)";
  	this.style.opacity = 1;
    slides[current].classList.toggle('make_z_index');
    current = parseInt(this.dataset.indexNumber);
    slides[current].classList.toggle('make_z_index');
    thumbnailList[current+1].style.boxShadow = "1px 2px 2px 0px rgba(181,125,125,1)";
  });
});

var menu = document.querySelectorAll('.thumb')
console.log(menu);
var thefirstChild = menu[0];
console.log(thefirstChild);


document.onkeydown = checkKey;
function checkKey(e) {
  e = e || window.event;
  if (e.keyCode == '38') {
      // up arrow
    callPrevious();
  }
  else if (e.keyCode == '40') {
      // down arrow
    callNext();
  }
  else if (e.keyCode == '37') {
     // left arrow
    callPrevious();
  }
  else if (e.keyCode == '39') {
     // right arrow
    callNext();
  }
}

//var nextSlider = document.querySelector('.thumb.next');

/*function OnMouseIn(nextSlider){
  footer.style.position = 'relative';
  footer.style.left = '-100px';
}*/
//OnMouseIn();
/*var newThumbArrowPrev = document.createElement('img');
newThumbArrowPrev.setAttribute('src', 'arrow.svg');
newThumbArrowPrev.setAttribute('class', 'thumb previous');
console.log(newThumbArrowPrev);
menu.appendChild(newThumbArrowPrev);

var newThumbArrowNext = document.createElement('img');
newThumbArrowNext.setAttribute('src', 'arrow.svg');
newThumbArrowNext.setAttribute('class', 'thumb next');
menu.appendChild(newThumbArrowNext);*/
