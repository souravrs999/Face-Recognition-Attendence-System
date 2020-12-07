#! env/usr/bin python

""" Necessary Imports """
import os
import cv2

""" function to create data folder """


def assure_path_exists(path):
    dir = os.path.dirname(path)

    """ if it does not exist create it """
    if not os.path.exists(dir):
        os.makedirs(dir)


""" Function to draw frame around face """


def draw_frame(img, pt1, pt2, color, thick, r, d):
    x1, y1 = pt1
    x2, y2 = pt2

    """ Top left """
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thick)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thick)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thick)

    """ Top right """
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thick)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thick)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thick)

    """ Bottom left """
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thick)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thick)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thick)

    """ Bottom right """
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thick)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thick)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thick)


""" A function to capture datat from webcam """


def capture_data(name, reg_id, src=1):

    """ Grab the frame from the camera """
    cap = cv2.VideoCapture(src)

    """ Declare variables """
    face_detector = cv2.CascadeClassifier("model/haarcascade_frontalface_default.xml")
    img_count = 0
    total_img_count = 200
    assure_path_exists("data/")

    while True:

        """ Grab frame """
        ret, frame = cap.read()

        if ret:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                draw_frame(frame, (x, y), (x + w, y + h), (255, 255, 255), 2, 10, 10)
                img_count += 1
                count_text = f"count: {img_count}/{total_img_count}"
                cv2.putText(
                    frame,
                    count_text,
                    (x + 20, y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    2,
                )
                cv2.imwrite(
                    "data/" + str(name) + "-" + str(reg_id) + "-" + str(count) + ".jpg",
                    gray[y : y + h, x : x + w],
                )

                if img_count > total_img_count:
                    break

            _, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
