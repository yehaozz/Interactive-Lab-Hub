#!/usr/bin/env python
from importlib import import_module
import os
import sys
import signal
import socket
# import pygame
from flask import Flask, render_template, Response, send_file
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call

Camera = import_module('camera.camera_opencv').Camera
camera = Camera()
hostname = socket.gethostname()

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/<audio_file_name>')
def returnAudioFile(audio_file_name):
    path_to_audio_file = "/home/pi/Interactive-Lab-Hub/project/music/" + audio_file_name
    return send_file(
         path_to_audio_file, 
         mimetype="audio/mpeg", 
         as_attachment=True, 
         attachment_filename="test.mp3")


@socketio.on('speak')
def handel_speak(val):
    command = """
        say() { 
            local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; 
        } ; 
    """ + f"say '{val}'"
    call(command, shell=True)


@socketio.on('ping_camera')
def handle_ping_camera(val):
    emit('pong_camera', camera.hand_exsit)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', threaded=True)
    socketio.run(app, host='0.0.0.0', port=5000)



# pygame.mixer.init()
# pygame.mixer.music.load("./music/Yi_Jian_Mei.mp3")

# @socketio.on('music_play')
# def handel_music_play():
#     pygame.mixer.music.play(-1)


# @socketio.on('music_pause')
# def handel_music_pause():
#     pygame.mixer.music.pause()


# @socketio.on('music_unpause')
# def handel_music_unpause():
#     pygame.mixer.music.unpause()


# @socketio.on('connect')
# def test_connect():
#     print('connected')
#     emit('after connect',  {'data':'Lets dance'})


# def signal_handler(sig, frame):
#     pygame.mixer.music.stop()
#     print('Closing Gracefully')
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)