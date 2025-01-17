// setup socket
const socket = io();
socket.on('connect', () => {

});

// socket disconnect
socket.on('disconnect', () => {
  console.log('disconnect')
});

const wordsIn = document.getElementById('wordsIn');

// Speak section send button onclick 
speak.onclick = () => {
  socket.emit('speak', wordsIn.value)
  wordsIn.value = ''
}
wordsIn.onkeyup = (e) => { if (e.keyCode === 13) { speak.click(); } }

const emotion = document.getElementById('emotion')

setInterval(() => {
  socket.emit('ping_camera', 'dat')
}, 100)

socket.on('pong_camera', label => {
  emotion.innerHTML = label
});

// music_play.onclick = () => {
//   socket.emit('music_play')
// }

// music_pause.onclick = () => {
//   socket.emit('music_pause')
// }

// music_unpause.onclick = () => {
//   socket.emit('music_unpause')
// }