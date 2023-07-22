import cv2
# import torch
import numpy as np
from keras.models import load_model
import os


basedir = os.path.abspath(os.path.dirname(__file__))
model = load_model(os.path.join(basedir+"/keras_Model.h5"), compile=False)
model.make_predict_function()         # Necessary
# print('Model loaded. Start serving...')
# Load the labels
class_names = open(os.path.join(basedir+"/labels.txt"), "r").readlines()


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
#        self.video = cv2.resize(self.video,(840,640))
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        image = cv2.flip(image, -1)
        results = model(image)
        a = np.squeeze(results.render())

        
       
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    