var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var matterPlayer;
var planningPlayer;

// Função chamada quando a API do YouTube está pronta
function onYouTubeIframeAPIReady() {
  const larguraTela = window.innerWidth;
  let height = '360';
  let width = '640';

  if (larguraTela < 600) {
    height = '240';
    width = '340';
  }

  matterPlayer = new YT.Player('matterHelp', {
    height: height,
    width: width,
    videoId: '9e8NdD9mM-Y',
    playerVars: {
      autoplay: 0,
    },
    events: {
      'onStateChange': onPlayerStateChange,
    },
  });

  planningPlayer = new YT.Player('plannerHelp', {
    height: height,
    width: width,
    videoId: 'BYJlLYDZrDw',
    playerVars: {
      autoplay: 0,
    },
    events: {
      'onStateChange': onPlayerStateChange,
    },
  });
  
  planningPlayer = new YT.Player('knowUs', {
    height: height,
    width: width,
    videoId: 'BYJlLYDZDw',
    playerVars: {
      autoplay: 0,
    },
    events: {
      'onStateChange': onPlayerStateChange,
    },
  });
}

function onPlayerReady(event) {
  event.target.playVideo();
}

var done = true;
function onPlayerStateChange(event) {
  if (event.data == YT.PlayerState.PLAYING && !done) {
    setTimeout(stopVideo, 6000, event.target);
    done = true;
  }
}

function stopVideo(player) {
  player.stopVideo();
}      