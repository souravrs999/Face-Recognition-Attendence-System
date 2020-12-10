<div align="center">
<img  src="media/autolog-logo.png">

<p style="color: #323232">
A python flask based project to make attendence logging an easy task. Powered by OpenCV and python in the backend and Bulma a cool opensource CSS framework based on Flexbox in the frontend.
</p>
</div>

<p align="center">
<a href="#">
<img src="https://img.shields.io/badge/PYTHON-3.8-f50057.svg?style=for-the-badge" alt="made with python">
</a>
<a href="#">
<img src="https://img.shields.io/badge/FLASK-1.1.2-f50057.svg?style=for-the-badge">
</a>
<a href="#">
<img src="https://img.shields.io/badge/BULMA-v0.9.1-f50057.svg?style=for-the-badge">
</a>
<a href="#">
<img src="https://img.shields.io/badge/OpenCV-4.2-f50057.svg?style=for-the-badge">
</a>
<a href="#">
<img src="https://img.shields.io/badge/DLIB-19.21-f50057.svg?style=for-the-badge">
</a>
<a href="#">
<img src="https://img.shields.io/badge/SQLAlchemy-1.3.20-f50057.svg?style=for-the-badge">
</a>
</p>

#### !!! Not Finished Yet !!!

##### Current status

<p style="color: #323232"> Index </p>
<img src="/media/index.png" style="float: center; margin-right: 10px;" width="1000"/>

<p style="color: #323232"> Login </p>
<img src="/media/login.png" style="float: center; margin-right: 10px;" width="1000"/>

<p style="color: #323232"> Sign Up </p>
<img src="/media/signup.png" style="float: center; margin-right: 10px;" width="1000"/>

##### Development

<div align="center">
<p style="color: #323232"> Here is the link to the app hosted on Heroku.</p>
<a href="https://faceregister.herokuapp.com/" target="_blank">
<img width=30% src="media/heroku-logo.png">
</a>
<p style="color: #323232">Note: The app might not be up at all time since it is still on development and might even be broken ! </p>
</div>

##### Readability

I've added comments for each and every line to the code to improve its readability for new users and for developers who might prefer to scale it in the future. It's completely modular and you can customize it for your use cases easily and effortlessly.

```python

#! env/usr/bin python

""" Necessary Imports """
import os
import cv2
import numpy as np

data_dir = "data/"
face_detector = cv2.CascadeClassifier("model/haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

""" function to create data folder """


def assure_path_exists(path):
    dir = os.path.dirname(path)

    """ if it does not exist create it """
    if not os.path.exists(dir):
        os.makedirs(dir)


""" Function to draw text in an image """


def put_text(img, text, coords, color):

    cv2.putText(
        img,
        text,
        coords,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        color,
        2,
    )


""" Function to parse Images and Labels """


def get_images_and_labels(data_dir):

    """Initialize empty arrays to hold our face samples
    and their respective ids"""
    face_samples, ids = [], []

    """ for each image in our data dir """
    for imgs in os.listdir(data_dir):
        img = os.path.join(data_dir, imgs)

        """ read the image using cv in grayscale """
        cv_img = cv2.imread(img, 0)

        """convert it into a numpy array """
        np_img = np.array(cv_img, "uint8")

        """ extract the image id from the name """
        Id = int(img.split("/")[1].split("-")[1])

        """ append the face samples and ids to the arrays """
        face_samples.append(np_img)
        ids.append(Id)

        return face_samples, ids


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


def capture_data(name, reg_id, src=1, ext_window=True):

    """ Grab the frame from the camera """
    cap = cv2.VideoCapture(src)

    """ Declare variables """

    ext_window = True
    img_count = 0
    total_img_count = 200
    assure_path_exists(data_dir)

    while True:

        """ Grab frame """
        ret, frame = cap.read()

        """ If it returned true """
        if ret:

            """ Convert the frame to grayscale easy to work on """
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            """ Detect all the faces """
            faces = face_detector.detectMultiScale(
                gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30)
            )

            """ for each detected face """
            for (x, y, w, h) in faces:

                """ draws the frame around their face """
                draw_frame(frame, (x, y), (x + w, y + h), (255, 255, 255), 2, 10, 10)

                """ increment the counter """
                img_count += 1
                count_text = f"count: {img_count}/{total_img_count}"

                """ write the total no of images grabbed to the frame """
                img = put_text(
                    frame,
                    count_text,
                    (x + 20, y - 20),
                    (255, 255, 255),
                )

                """ Save these faces frames to the data folder which
                can be used to train the LBPH face recognizer """
                img_name = f"{str(name)}-{str(reg_id)}-{str(img_count)}.jpg"
                cv2.imwrite(
                    os.path.join(data_dir, img_name),
                    gray[y : y + h, x : x + w],
                )

                """ If ext_win flag is set show external window
                will not work on server without native cams """
                if ext_window:
                    cv2.imshow("data_capture", frame)

            """ if the img count recieved our necessary limit break the loop """
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            elif img_count > total_img_count:
                break

            """ encode the frames to bytes to display it """
            _, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"

    cap.release()
    cv2.destroyAllWindows()


""" Function to train the face recognition model """


def train_model():

    """ get the face samples and ids for training """
    face_samples, ids = get_images_and_labels(data_dir)

    """ train the model """
    face_recognizer.train(face_samples, np.array(ids))
```

:pen:
