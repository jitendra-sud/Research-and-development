from flask import Flask, Response, render_template, request
import numpy as np
from camera import Video 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')


@app.route('/video')

def video():
    return Response(gen(Video()), 
    mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/detect', methods=['POST', 'GET'])
# def func():
#     img = request.form['img']
#     # print(img)
#     cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
#     # i = imageio.v2.imread(img)
#     # ap = argparse.ArgumentParser()
#     # ap.add_argument("-c", "--confidence", type=float, default=0.2,help="minimum probability to filter weak detections")
#     # args = vars(ap.parse_args())

#     # cv2.imshow("Output",img)
#     # cv2.waitKey(0) 

#     # cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    
#     print("[INFO] loading model architecture and weights...")
#     # proto = 'deploy.prototxt.txt'
#     # model = 'res10_300x300_ssd_iter_140000.caffemodel'
#     args= {
# "image":img,


# "prototxt":"deploy.prototxt.txt",


# "model":"res10_300x300_ssd_iter_140000.caffemodel",


# "confidence":0.9


# }
#     net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
    
#     while True:
#         print("[INFO] Processing input image...")
#         # image = Image.open(args["image"])

#         image = cv2.imread(args["image"])
#         (h, w) = image.shape[:2]
#         blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))

#         print("[INFO] computing object detections...")
#         net.setInput(blob)
#         detections = net.forward()

#         print("[INFO] Looping over object detections...")
#         for i in range(0, detections.shape[2]):
#             confidence = detections[0,0,i,2]
#             if confidence > args["confidence"]:
#                 box = detections[0,0,i,3:7] * np.array([w,h,w,h])
#                 (startX, startY, endX, endY) = box.astype("int")

#                 text = "{:.2f}%".format(confidence*100)
#                 y = startY - 10 if startY - 10  > 10 else startY + 10
#                 cv2.rectangle(image,(startX, startY), (endX,endY),(0,0,225),2)
#                 cv2.putText(image,text,(startX,y),cv2.FONT_HERSHEY_SIMPLEX, 0.45,(0,0,225), 2)
    
        
#         # data  = io.BytesIO()
#         # image.save(data,"JPEG")
#         # encoded_img_data = base64.b64encode(data.getvalue())

        
#         i = cv2.imshow("Output",image) 
#         # key = cv2.waitKey(0)
#         # if key == ord('q'):
#         #     break
#         # cv2.destroyAllWindows()
#         return render_template("index.html",image = i)
        


if __name__ == "__main__":
    app.run(debug=True)
