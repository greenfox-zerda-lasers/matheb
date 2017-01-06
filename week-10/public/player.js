var playLists = document.querySelector(".playlist_elements")
var trackList = document.querySelector(".tracks")
var audio = document.querySelector("audio");

var title = document.querySelector(".current_title");
var musician = document.querySelector(".musician");

var dialog = document.querySelector(".addToPlaylist");
var dialogInput = document.querySelector(".addNewPlaylist");

var tracks = document.querySelectorAll(".track");
console.log(tracks)
var playlist_divs = document.querySelectorAll(".playlist_item");
var playlist_elements = document.querySelector(".playlist_elements");
var currentPlaylist = 0;
var currentTrack = 0;

// tracks loaded from server via AJAX
var playlistData = []
var playlistDataLength = playlistData.length; // tracks loaded from server via AJAX
var tracks = document.querySelectorAll(".track")

//var audio = new Audio();
var audio = document.querySelector('audio');

var playButton = document.querySelector("#play-pause");
var prevButton = document.querySelector("#rewind");
var nextButton = document.querySelector("#forward");
var track_length = document.querySelector(".track-length");
var time = document.querySelector(".time");

function loadTracks(Tracklist, Listlength){
  trackList.innerHTML = '';
  for (var i = 0; i < Listlength; i++){
    audio.volume = 1;
    var newTrack = document.createElement('div');
    newTrack.setAttribute('data-index-Number', i);
    newTrack.textContent = Tracklist[i]['title'];
    if (i === 0 ){
      newTrack.setAttribute('class', 'track active darker');
    } else if (i%2 === 0) {
      newTrack.setAttribute('class', 'track  darker')
    } else {
      newTrack.setAttribute('class', 'track transparent');
    }
    trackList.appendChild(newTrack);
    tracks = document.querySelectorAll(".track");
    newTrack.addEventListener('click', function () {
      console.log(currentTrack)
      tracks[currentTrack].classList.toggle('active')
      currentTrack = parseInt(this.dataset.indexNumber);
      tracks[currentTrack].classList.toggle('active')
      audio.setAttribute('src', Tracklist[this.dataset.indexNumber]['path']);
      title.textContent = Tracklist[this.dataset.indexNumber]['title'];
      musician.textContent = Tracklist[this.dataset.indexNumber]['artist'];
      audio.play();
    })
    console.log(tracks)
    console.log(Tracklist)
  }
  nextButton.addEventListener('click', function () {
    callNext(Tracklist, Listlength, tracks);
  })
  prevButton.addEventListener('click', function () {
    callPrev(Tracklist, Listlength, tracks);
  })
}
//loadTracks();


var DelButton = ( function () {

  function createDel() {

    var newDelButton = document.createElement('img');
    newDelButton.setAttribute('src', "buttons/quit_icon.png");
    newDelButton.setAttribute('class', "del");
    newDelButton.addEventListener('click', function() {
      removePlaylist(this.dataset.indexNumber, loadPlaylists);
    });
    return newDelButton
  }

  return {
    button: createDel
  };

})();


function loadPlaylists(Playlists, Listlength){
  //console.log(playList)
  playLists.innerHTML = '';
  tracks.innerHTML = '';
  var playlist_divs = [];
  for (var i = 0; i < Listlength; i++){
    var newPlaylist = document.createElement('div');
    var newPlaylistName = document.createElement('div');
    var newTrackButton = document.createElement('div');
    newPlaylist.setAttribute('data-index-Number', Playlists[i]['id']);
    newPlaylist.setAttribute('data-column', i);
    newPlaylist.textContent = Playlists[i]['playlist'];
    newPlaylist.addEventListener('click', getTracklist);
    if (i > 1){
      var db = DelButton.button();
      db.setAttribute('data-index-Number', Playlists[i]['id']);
      newPlaylist.appendChild(db);
    }
    newTrackButton.setAttribute('class', 'button');
    newTrackButton.setAttribute('data-index-Number', Playlists[i]['id']);
    newTrackButton.setAttribute('data-column', i);
    newTrackButton.textContent = Playlists[i]['playlist'];
    newTrackButton.addEventListener('click', function(){
      postTrack(this);
      getTracklist(playlist_divs[currentPlaylist]);
      console.log(playlist_divs[currentPlaylist]);
    });
    if (i === 0 ){
      newPlaylist.setAttribute('class', 'playlist_item active darker');
    } else if (i%2 === 0) {
      newPlaylist.setAttribute('class', 'playlist_item  darker')
    } else {
      newPlaylist.setAttribute('class', 'playlist_item transparent');
    }
    //changePlaylistOption();
    // newPlaylist.addEventListener('click', function(e) {
    //   Playlists[currentPlaylist].classList.toggle('active')
    //   currentTrack = parseInt(this.dataset.indexNumber);
    //   Playlists[currentPlaylist].classList.toggle('active')
    // })
    playLists.appendChild(newPlaylist);
    dialog.appendChild(newTrackButton);
    playlist_divs.push(newPlaylist);

    newPlaylist.addEventListener('click', function () {
      console.log(currentPlaylist)
      playlist_divs[currentPlaylist].classList.toggle('active')
      currentPlaylist = parseInt(this.dataset.column);
      playlist_divs[currentPlaylist].classList.toggle('active')
      getTracklist(this)
    })
  }
  // audio.setAttribute('src', musicList[0]['src']);
}
//loadPlaylists();

console.log(tracks);
tracks.forEach(function(item,index){
  tracks[index].addEventListener('click', function(e) {
    tracks[currentTrack].classList.toggle('active')
    currentTrack = parseInt(this.dataset.indexNumber);
    tracks[currentTrack].classList.toggle('active')
    audio.setAttribute('src', musicList[currentTrack]['src']);
    title.textContent = musicList[currentTrack]['title'];
    musician.textContent = musicList[currentTrack]['musician'];
  });
});

playlist_divs.forEach(function(item,index){
  playlist_divs[index].addEventListener('click', function(e) {
    playlist_divs[currentPlaylist].classList.toggle('active')
    currentPlaylist = parseInt(this.dataset.indexNumber);
    playlist_divs[currentPlaylist].classList.toggle('active')
  });
});

function changePlaylistOption (newPlaylist) {
  newPlaylist.addEventListener('click', function(e) {
    playlist_divs[currentPlaylist].classList.toggle('active')
    currentPlaylist = parseInt(this.dataset.indexNumber);
    playlist_divs[currentPlaylist].classList.toggle('active')
  });
}

var addTrack = document.querySelectorAll(".add_icon")[1];
var addPlaylist = document.querySelectorAll(".add_icon")[0];
var quitButton1 = document.querySelector(".quit1");
var quitButton2 = document.querySelector(".quit2");
console.log(addTrack);

addTrack.addEventListener('click', function(){
  dialog.style.visibility = "visible";
})

addPlaylist.addEventListener('click', function(){
  dialogInput.style.visibility = "visible";
})

quitButton1.addEventListener('click', function(){
  dialogInput.style.visibility = "hidden";
})

quitButton2.addEventListener('click', function(){
  dialog.style.visibility = "hidden";
})

var addFavorite = document.querySelectorAll(".star_icon")[0];
addFavorite.addEventListener('click', function(){
  alert('Do you want to add the Track to Favourites?');
})


// AJAX CALLLSS TRY

function getPlayList(){
  var xhr = new XMLHttpRequest();
  xhr.open('GET', "http://localhost:3000/playlists", true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function (){
    if (xhr.readyState === XMLHttpRequest.DONE){
      var Playlists = JSON.parse(xhr.response);
      var Listlength = Playlists.length;
      loadPlaylists(Playlists, Listlength);
    }
  }
};
getPlayList();

console.log(playlist_divs)
var addButton = document.querySelector(".add");


function addNewPlaylist(){
  console.log(addButton)
  var req = new XMLHttpRequest();
  var input = document.querySelector("input.options").value;
  if (input != ''){
    name = input;
    req.open('POST', "http://localhost:3000/playlists", true);
    req.setRequestHeader("Content-Type", "application/json");
    req.onreadystatechange = function (){
      if (req.readyState === XMLHttpRequest.DONE){
        var Playlists = JSON.parse(req.response);
        var Listlength = Playlists.length;
        loadPlaylists(Playlists, Listlength);
        dialogInput.style.visibility = "hidden";
      }
    }
  }
  req.send(JSON.stringify({name: name}));
}
addButton.addEventListener('click', addNewPlaylist);

function removePlaylist(item, callback){
  var req = new XMLHttpRequest();
  req.open('DELETE', "http://localhost:3000/playlists/" +item, true);
  req.setRequestHeader("Accept", "application/json; charset=utf-8");
  req.send();
  req.onreadystatechange = function (){
    if (req.readyState === XMLHttpRequest.DONE){
      console.log(req.response);
      var Playlists = JSON.parse(req.response);
      var Listlength = Playlists.length;
      callback(Playlists, Listlength);
    }
  }
};

function getTracklist(item){
  // console.log(item.dataset.indexNumber)
  item.playlist_id = item.dataset.indexNumber;
  var xhr = new XMLHttpRequest();
  xhr.open('GET', "http://localhost:3000/playlist-tracks/"+item.playlist_id, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function (){
    if (xhr.readyState === XMLHttpRequest.DONE){
      var Tracklist = JSON.parse(xhr.response);
      playlistData = Tracklist;
      var Listlength = Tracklist.length;
      console.log(Tracklist)
      loadTracks(Tracklist, Listlength);
    }
  }
};

function findPath(playlistData, item) {
  for (var i = 0; i < playlistData.length; i++){
    console.log(item.column);
    if ( item.column === playlistData[currentTrack]){
      return playlistData[currentTrack].path;
    }
  }
}

function postTrack(item){
  item.playlist_id = item.dataset.indexNumber;
  var path = playlistData[currentTrack]['path'];
  var title = playlistData[currentTrack]['title']
  var artist = playlistData[currentTrack]['artist']
  var xhr = new XMLHttpRequest();
  xhr.open('POST', "http://localhost:3000/playlist-tracks/"+item.playlist_id, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({path: path, title: title, artist: artist}));
  xhr.onreadystatechange = function (){
    if (xhr.readyState === XMLHttpRequest.DONE){
      var Tracklist = JSON.parse(xhr.response);
      var Listlength = Tracklist.length;
      loadTracks(Tracklist, Listlength);
    }
  }
  dialog.style.visibility = "hidden";
};

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

playButton.addEventListener('click', function(e)
{
  //console.log(Tracklist)
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


function callNext(Tracklist, Listlength, tracks){
  if (currentTrack === Listlength-1){
    tracks[currentTrack].classList.toggle('active')
    currentTrack = 0;
    tracks[currentTrack].classList.toggle('active')
    console.log(Tracklist[this.dataset.indexNumber])
    audio.setAttribute('src', Tracklist[currentTrack]['path']);
    title.textContent = Tracklist[currentTrack]['title'];
    musician.textContent = Tracklist[currentTrack]['artist'];
    track_length.textContent = audio.duration;
  } else {
    console.log(tracks)
    tracks[currentTrack].classList.toggle('active')
    currentTrack++;
    tracks[currentTrack].classList.toggle('active')
    audio.setAttribute('src', Tracklist[currentTrack]['path']);
    title.textContent = Tracklist[currentTrack]['title'];
    musician.textContent = Tracklist[currentTrack]['artist'];
    track_length.textContent = audio.duration;
  }
  audio.play();
};

function callPrev(Tracklist, Listlength, tracks) {
  if (currentTrack > 0){
    tracks[currentTrack].classList.toggle('active')
    currentTrack --;
    tracks[currentTrack].classList.toggle('active')
    audio.setAttribute('src', Tracklist[currentTrack]['src']);
    audio.play();
    playButton.setAttribute('src', 'buttons/pause.svg');
    title.textContent = Tracklist[currentTrack]['title'];
    musician.textContent = Tracklist[currentTrack]['musician'];
  } else {
    tracks[currentTrack].classList.toggle('active')
    currentTrack = Listlength-1;
    tracks[currentTrack].classList.toggle('active')
    audio.setAttribute('src', Tracklist[currentTrack]['src']);
    audio.play();
    playButton.setAttribute('src', 'buttons/pause.svg');
    title.textContent = Tracklist[currentTrack]['title'];
    musician.textContent = Tracklist[currentTrack]['musician'];
  }
};

audio.addEventListener("canplaythrough", function()
{
  audio.play();
  console.log("canplaythrough event happened");
}, true);

audio.addEventListener("loadstart", function()
{
  console.log("loadstart event happened");
}, true);
