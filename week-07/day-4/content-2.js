// fill every paragraph with the last one's content.
var paragraphs = document.getElementsByTagName("p");
for (var i = 0; i < paragraphs.length; i++){
  paragraphs[i].textContent = paragraphs[paragraphs.length-1].textContent;
};
