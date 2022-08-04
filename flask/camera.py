import numpy as np
import argparse
import imutils
import time
import cv2

class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release() 
    def get_frame(self):
        ret,frame = self.video.read()
        args= {
            "prototxt":"deploy.prototxt.txt",
            "model":"res10_300x300_ssd_iter_140000.caffemodel",
            "confidence":0.9
        }
        print("[INFO] loading model...")
        net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

        print("[INFO] starting video stream...")

        vid=frame
        while True:
            ret,fr = vid.read()
            fr=imutils.resize(fr,width=400)

            (h,w) = fr.shape[:2]
            blob = cv2.dnn.blobFromeImage(cv2.resize(fr,(300,300)), 1.0, (300,300), (104.0,177.0,123.0))

            net.setInput(blob)
            detections = net.forword()

            for i in range(0, detections.shape[2]):
                confidence = detections[0,0,i,2]

                if confidence < args["confidence"]:
                    continue

                box = detections[0,0,i,3:7] * np.array([w,h,w,h])
                (startX, startY, endX, endY) = box.astype("int")

                text = "{:.2f}%".format(confidence * 100)
                y = startY - 10 if startY -10 > 10 else startY + 10 
                cv2.rectangle(fr, (startX,startY), (endX,endY), (0, 0, 255), 2)
                cv2.putText(fr, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

            ret,jpg = cv2.imencode('.jpg',fr)
            return jpg.tobytes()


        
            



