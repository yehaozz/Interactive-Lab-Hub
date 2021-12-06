# from https://blog.miguelgrinberg.com/post/video-streaming-with-flask
import os
import cv2
from .base_camera import BaseCamera
from .HandTrackingModule import handDetector


class Camera(BaseCamera):
    video_source = 0
    detector = handDetector(detectionCon=0.7)
    hand_exsit = False

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            img = Camera.detector.findHands(img)
            lmList = Camera.detector.findPosition(img, draw=False)
            Camera.hand_exsit = len(lmList) > 0

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
