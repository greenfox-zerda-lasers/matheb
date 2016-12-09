var collection = [
  {
    title: "Pond of Reykjavik",
    explanation: "Wonderful weather at one og the last days of August 2016",
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


function fillContent(){
  var contentList = document.querySelector(".bigPhoto");
  var footer = document.querySelector(".pics");

  for (var i = 0; i < collection.length; i++){
    var newImage = document.createElement('img');
    newImage.setAttribute('src', collection[i]['src']);
    contentList.appendChild(newImage);

    var newThumb = document.createElement('img');
    newThumb.setAttribute('src', collection[i]['src']);
    newThumb.setAttribute('class', "thumb");
    footer.appendChild(newThumb);

    var exp = document.createElement('section');
    exp.setAttribute('class', 'current');

    var newTitle = document.createElement('h1');
    if (i === 0){
      newTitle.setAttribute('class', 'make_z_index');
    };
    newTitle.textContent = collection[i]['title'];
    exp.appendChild(newTitle);

    var newPar = document.createElement('p');
    if (i === 0){
      newPar.setAttribute('class', 'make_z_index');
    };
    newPar.textContent = collection[i]['explanation'];
    exp.appendChild(newPar);

    contentList.appendChild(exp);
  };
  //return contentList;
};

fillContent();
