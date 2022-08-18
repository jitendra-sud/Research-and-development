import numpy as np
import imutils
import cv2

class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release() 
    def get_frame(self):
        ret,frame = self.video.read()

        age_weights = "age_deploy.prototxt"
        age_config = "age_net.caffemodel"
        ageNet = cv2.dnn.readNet(age_config, age_weights)
        ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
        # mssg = 'Face Detected'

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
            fr = vid
            fr=imutils.resize(fr,width=700)

            (h,w) = fr.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(fr,(300,300)), 1.0, (300,300), (104.0,177.0,123.0))

            net.setInput(blob)
            detections = net.forward()

            for i in range(0, detections.shape[2]):
                confidence = detections[0,0,i,2]

                if confidence < args["confidence"]:
                    continue

                box = detections[0,0,i,3:7] * np.array([w,h,w,h])
                (startX, startY, endX, endY) = box.astype("int")

                face = fr[startY:endY, startX:endX]
                faceBlob = cv2.dnn.blobFromImage(face, 1.0, (227, 227),(78.4263377603, 87.7689143744, 114.895847746),swapRB=False)

                ageNet.setInput(faceBlob)
                preds = ageNet.forward()
                i = preds[0].argmax()
                age = ageList[i]
                ageConfidence = preds[0][i]

                text = "{}: {:.2f}%".format(age, ageConfidence * 100)
                print("[INFO] {}".format(text))

               
                y = startY - 10 if startY -10 > 10 else startY + 10 
                cv2.rectangle(fr, (startX,startY), (endX,endY), (0, 0, 255), 2)
                cv2.putText(fr, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)          
               
            

            ret,jpg = cv2.imencode('.jpg',fr)
            return jpg.tobytes()


        




