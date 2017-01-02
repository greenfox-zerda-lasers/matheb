var audio = document.querySelector("audio");

audio.addEventListener('ended', function(e)
{
  audio.pause();
  console.log("ended event happened");
}, false);

audio.addEventListener("play", function()
{
  audio.play();
  console.log("play event happened");
}, true);

audio.addEventListener("pause", function()
{
  audio.pause();
  console.log("pause event happened");
}, true);

audio.addEventListener("canplaythrough", function()
{
  //audio.play();
  console.log("canplaythrough event happened");
}, true);

audio.addEventListener("loadstart", function()
{
  console.log("loadstart event happened");
}, true);


audio.addEventListener('progress', function()
{
  var ranges = [];
  for(var i = 0; i < audio.buffered.length; i ++)
  {
    ranges.push([
      audio.buffered.start(i),
      audio.buffered.end(i)
      ]);
  }
  console.log("progress event happened");
}, false);
