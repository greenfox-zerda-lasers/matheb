// Initialize a new plugin instance for element or array of elements.
var slider = document.querySelectorAll('input[type="range"]');
rangeSlider.create(slider[0], {
  polyfill: true,     // Boolean, if true, custom markup will be created
  rangeClass: 'rangeSlider',
  disabledClass: 'rangeSlider--disabled',
  fillClass: 'rangeSlider__fill',
  bufferClass: 'rangeSlider__buffer',
  handleClass: 'rangeSlider__handle',
  startEvent: ['mousedown', 'touchstart', 'pointerdown'],
  moveEvent: ['mousemove', 'touchmove', 'pointermove'],
  endEvent: ['mouseup', 'touchend', 'pointerup'],
  min: null,          // Number , 0
  max: null,          // Number, 100
  step: null,         // Number, 1
  value: null,        // Number, center of slider
  buffer: null,       // Number, in percent, 0 by default
  stick: null,        // [Number stickTo, Number stickRadius] : use it if handle should stick to stickTo-th value in stickRadius
  borderRadius: 10,    // Number, if you use buffer + border-radius in css for looks good,
  onInit: function () {
    console.info('onInit')
  },
  onSlideStart: function (position, value) {
    console.info('onSlideStart', 'position: ' + position, 'value: ' + value);
  },
  onSlide: function (position, value) {
    console.log('onSlide', 'position: ' + position, 'value: ' + value);
  },
  onSlideEnd: function (position, value) {
    console.warn('onSlideEnd', 'position: ' + position, 'value: ' + value);
  }
});

var muteSong = document.querySelector("#volume-bar")
rangeSlider.create(slider[1], {
  polyfill: true,     // Boolean, if true, custom markup will be created
  rangeClass: 'rangeSlider',
  disabledClass: 'rangeSlider--disabled',
  fillClass: 'rangeSlider__fill',
  bufferClass: 'rangeSlider__buffer',
  handleClass: 'rangeSlider__handle',
  startEvent: ['mousedown', 'touchstart', 'pointerdown'],
  moveEvent: ['mousemove', 'touchmove', 'pointermove'],
  endEvent: ['mouseup', 'touchend', 'pointerup'],
  min: null,          // Number , 0
  max: null,          // Number, 100
  step: null,         // Number, 1
  value: null,        // Number, center of slider
  buffer: null,       // Number, in percent, 0 by default
  stick: null,        // [Number stickTo, Number stickRadius] : use it if handle should stick to stickTo-th value in stickRadius
  borderRadius: 10,    // Number, if you use buffer + border-radius in css for looks good,
  onInit: function () {
    console.info('onInit')
  },
  // onSlideStart: function (position, value) {
  //   console.info('onSlideStart', 'position: ' + position, 'value: ' + value);
  // },
  onSlide: function (position, value) {
    console.log('onSlide', 'position: ' + position, 'value: ' + value);
    audio.volume = value;
    if (value === 0){
      muteSong.style.backgroundImage = "url(images/mute_new.svg)";
      muteSong.style.backgroundSize = '20px';
    } else {
      muteSong.style.backgroundImage = "url(images/volume.svg)";
      muteSong.style.backgroundSize = '10px';
    }
  },
  // onSlideEnd: function (position, value) {
  //   console.warn('onSlideEnd', 'position: ' + position, 'value: ' + value);
  // }
});

// then...
// var giveMeSomeEvents = true; // or false
// slider.rangeSlider.update({min : 0, max : 20, step : 0.5, value : 1.5, buffer : 70}, giveMeSomeEvents);
// // or
/* slider.rangeSlider.onSlideStart: function (position, value) {
  console.error('anotherCallback', 'position: ' + position, 'value: ' + value);
} */

var audio = new Audio();
audio.src = musicList[0]['src'];
audio.volume = 1;
audio.play();
var playButton = document.querySelector("#play-pause");
var prevButton = document.querySelector("#rewind");
var nextButton = document.querySelector("#forward");
var track_length = document.querySelector(".track-length");
var time = document.querySelector(".time");
console.log(audio.duration);

audio.addEventListener('loadedmetadata',function(){
  track_length.textContent = Math.floor(audio.duration/60)+":"+Math.floor(audio.duration%60);
  console.log(audio.duration);
});

audio.addEventListener('ended', function(e)
{
  audio.pause();
  console.log("ended event happened");
}, false);

var tracks = document.querySelectorAll(".track");
var playlist_divs = document.querySelectorAll(".playlist_item");
var currentTrack = 0;
var currentPlaylist = 0;

console.log(tracks);
tracks.forEach(function(item,index){
  tracks[index].addEventListener('click', function(e) {
    tracks[currentTrack].classList.toggle('active')
    currentTrack = parseInt(this.dataset.indexNumber);
    tracks[currentTrack].classList.toggle('active')
    audio.setAttribute('src', musicList[currentTrack]['src']);
    audio.play();
    track_length.textContent = audio.duration;
  });
});

playButton.addEventListener('click', function(e)
{
  if(audio.paused)
  {
    audio.play();
    playButton.setAttribute('src', 'buttons/pause.svg');
  }
  else
  {
    audio.pause();
    playButton.setAttribute('src', 'buttons/play.svg');
  }

}, false);

var title = document.querySelector(".current_title");
var musician = document.querySelector(".musician");
title.textContent = musicList[currentTrack]['title'];
musician.textContent = musicList[currentTrack]['musician'];

prevButton.addEventListener('click', function(){
  if (currentTrack > 0){
    tracks[currentTrack].classList.toggle('active')
    currentTrack --;
    tracks[currentTrack].classList.toggle('active')
    audio.setAttribute('src', musicList[currentTrack]['src']);
    audio.play();
    playButton.setAttribute('src', 'buttons/pause.svg');
    title.textContent = musicList[currentTrack]['title'];
    musician.textContent = musicList[currentTrack]['musician'];
  } else {
    tracks[currentTrack].classList.toggle('active')
    currentTrack = musicList.length-1;
    tracks[currentTrack].classList.toggle('active')
    audio.setAttribute('src', musicList[currentTrack]['src']);
    audio.play();
    playButton.setAttribute('src', 'buttons/pause.svg');
    title.textContent = musicList[currentTrack]['title'];
    musician.textContent = musicList[currentTrack]['musician'];
  }
})

nextButton.addEventListener('click', function(){
  if (currentTrack < musicList.length-1){
    tracks[currentTrack].classList.toggle('active')
    currentTrack ++;
    tracks[currentTrack].classList.toggle('active')
    audio.setAttribute('src', musicList[currentTrack]['src']);
    audio.play();
    playButton.setAttribute('src', 'buttons/pause.svg');
    title.textContent = tracks[currentTrack]['title'];
    musician.textContent = tracks[currentTrack]['musician'];
  } else {
    tracks[currentTrack].classList.toggle('active')
    currentTrack = 0;
    tracks[currentTrack].classList.toggle('active')
    audio.setAttribute('src', tracks[currentTrack]['src']);
    audio.play();
    playButton.setAttribute('src', 'buttons/pause.svg');
    title.textContent = tracks[currentTrack]['title'];
    musician.textContent = tracks[currentTrack]['musician'];
  }
})

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
