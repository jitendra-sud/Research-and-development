import numpy as np
import argparse
import imutils
import time
import cv2
from imutils .video import videostream

class Image(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release() 
    def get_frame(self):
        ret,frame = self.video.read()
        ret,jpg = cv2.imencode('.jpg',frame)
        return jpg.tobytes()

