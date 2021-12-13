# from https://blog.miguelgrinberg.com/post/video-streaming-with-flask
import os
import cv2
from .base_camera import BaseCamera
import numpy as np
import tensorflow.keras

def read_file():
    labels = []
    # f = open("/home/pi/idd-final/Interactive-Lab-Hub/Final_project/camera/labels.txt", "r")
    # f = open("camera/labels.txt", "r")
    f = open(os.path.join("camera", "labels.txt"), "r")
    for line in f.readlines():
        if(len(line)<1):
            continue
        labels.append(line.split(' ')[1].strip())
    return labels
    
class Camera(BaseCamera):
    video_source = 0
    # Load the model
    # model = tensorflow.keras.models.load_model('keras_model.h5')
    # model = tensorflow.keras.models.load_model('/home/pi/idd-final/Interactive-Lab-Hub/Final_project/camera/keras_model.h5')
    model = tensorflow.keras.models.load_model(os.path.join("camera", "keras_model.h5"))

    # Load Labels:
    labels = read_file()
    label = "Angry"

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
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            size = (224, 224)
            img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
            #turn the image into a numpy array
            image_array = np.asarray(img)

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            # Load the image into the array
            data[0] = normalized_image_array


            # run the inference
            prediction = Camera.model.predict(data)
            # print(prediction)
            # print(Camera.labels[np.argmax(prediction)])
            Camera.label = Camera.labels[np.argmax(prediction)]

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
