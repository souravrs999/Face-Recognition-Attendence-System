#! env/usr/bin python

""" Necessary Imports """
import os
import cv2

""" A function to capture datat from webcam """


def data_capture_fun(src=1):

    """ function to create data folder """

    def assure_path_exists(path):
        dir = os.path.dirname(path)

        """ if it does not exist create it """
        if not os.path.exists(dir):
            os.makedirs(dir)

    """ Grab the frame from our threaded videocapture class """
    cap = cv2.VideoCapture(src)

    """ Declare variables """
    face_detector = cv2.CascadeClassifier("model/haarcascade_frontalface_default.xml")
    img_count = 0

    assure_path_exists("data/")

    while True:

        """ Grab frame """
        ret, frame = cap.read()

        """ if it didnt return anything break """
        if not ret:
            break
        else:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            try:
                faces = face_detector.detectMultiScale(gray, 1.3, 5)
                line_color = (255, 255, 255)

                for (x, y, w, h) in faces:
                    cv2.line(frame, (x, y), (x, x + y + w / 4), line_color, 2)

            except Exception as e:
                print(e)

            _, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
