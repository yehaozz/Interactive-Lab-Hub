# from https://blog.miguelgrinberg.com/post/video-streaming-with-flask
import os
import cv2
from .base_camera import BaseCamera
import mediapipe as mp


class Camera(BaseCamera):
    video_source = 0
    hand_exsit = False
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_holistic = mp.solutions.holistic

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

        with Camera.mp_holistic.Holistic(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as holistic:
            while True:
                # read current frame
                success, image = camera.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    continue

                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = holistic.process(image)

                # Draw landmark annotation on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                Camera.mp_drawing.draw_landmarks(
                    image,
                    results.face_landmarks,
                    Camera.mp_holistic.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=Camera.mp_drawing_styles
                    .get_default_face_mesh_contours_style())
                Camera.mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    Camera.mp_holistic.POSE_CONNECTIONS,
                    landmark_drawing_spec=Camera.mp_drawing_styles
                    .get_default_pose_landmarks_style())
                # Flip the image horizontally for a selfie-view display.
                cv2.flip(image, 1)

                # encode as a jpeg image and return it
                yield cv2.imencode('.jpg', image)[1].tobytes()
