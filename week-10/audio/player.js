var musicList = [
  {
    title: "Never give up",
    src: "ars.mp3"
  },
  {
    title: "Purple drift",
    src: "purple.mp3"
  },
  {
    title: "Doctor Talos answers the door",
    src: "doctor.mp3"
  },
];

var playList = [ "All track", "Holiday", "Weekend"];
var playLists = document.querySelector(".playlist_elements")

var trackList = document.querySelector(".tracks")
var audio = document.querySelector("audio");
console.log(trackList);

function loadTracks(){
  for (var i = 0; i < musicList.length; i++){
    var newTrack = document.createElement('div');
    newTrack.setAttribute('data-index-Number', i);
    newTrack.textContent = musicList[i]['title'];
    if (i === 0){
      newTrack.setAttribute('class', 'track active');
      console.log("valami")
    } else {
      newTrack.setAttribute('class', 'track');
    }
    if (i%2 === 0){
      newTrack.style.backgroundColor = "lightgrey";
    } else {
      newTrack.style.background = "transparent";
    }
    trackList.appendChild(newTrack);
  }
  audio.setAttribute('src', musicList[0]['src']);
}
loadTracks();

function loadPlaylists(){
  for (var i = 0; i < playList.length; i++){
    var newPlaylist = document.createElement('div');
    newPlaylist.setAttribute('data-index-Number', i);
    newPlaylist.textContent = playList[i];
    if (i === 0){
      newPlaylist.setAttribute('class', 'playlist_item active');
      console.log("valami")
    } else {
      newPlaylist.setAttribute('class', 'playlist_item');
    }
    if (i%2 === 0){
      newPlaylist.style.backgroundColor = "lightgrey";
    } else {
      newPlaylist.style.background = "transparent";
    }
    playLists.appendChild(newPlaylist);

  }
  // audio.setAttribute('src', musicList[0]['src']);
}
loadPlaylists();

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
    audio.setAttribute('src', musicList[current]['src']);
  });
});

playlist_divs.forEach(function(item,index){
  playlist_divs[index].addEventListener('click', function(e) {
    playlist_divs[currentPlaylist].classList.toggle('active')
    currentPlaylist = parseInt(this.dataset.indexNumber);
    playlist_divs[currentPlaylist].classList.toggle('active')
  });
});