from ast import Break
from asyncore import read
from flask import Flask, render_template, request
from asyncore import read
import numpy as np
import cv2
import argparse
from PIL import Image
import imageio as imageio
 
# read an image



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST', 'GET'])
def func():
    img = request.form['img']
    # print(img)
    # cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    # i = imageio.v2.imread(img)
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-c", "--confidence", type=float, default=0.2,help="minimum probability to filter weak detections")
    # args = vars(ap.parse_args())

    # cv2.imshow("Output",img)
    # cv2.waitKey(0) 

    # cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    
    print("[INFO] loading model architecture and weights...")
    # proto = 'deploy.prototxt.txt'
    # model = 'res10_300x300_ssd_iter_140000.caffemodel'
    args= {
"image":img,


"prototxt":"deploy.prototxt.txt",


"model":"res10_300x300_ssd_iter_140000.caffemodel",


"confidence":0.9


}
    net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
    
    while True:
        print("[INFO] Processing input image...")
        image = cv2.imread(args["image"])
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))

        print("[INFO] computing object detections...")
        net.setInput(blob)
        detections = net.forward()

        print("[INFO] Looping over object detections...")
        for i in range(0, detections.shape[2]):
            confidence = detections[0,0,i,2]
            if confidence > args["confidence"]:
                box = detections[0,0,i,3:7] * np.array([w,h,w,h])
                (startX, startY, endX, endY) = box.astype("int")

                text = "{:.2f}%".format(confidence*100)
                y = startY - 10 if startY - 10  > 10 else startY + 10
                cv2.rectangle(image,(startX, startY), (endX,endY),(0,0,225),2)
                cv2.putText(image,text,(startX,y),cv2.FONT_HERSHEY_SIMPLEX, 0.45,(0,0,225), 2)
    

        # cv2.imshow("Output",image) 
        # key = cv2.waitKey(1)
        # if key == ord('q'):
        #     break
        return render_template("index.html",image=image)
        


if __name__ == "__main__":
    app.run(debug=True)