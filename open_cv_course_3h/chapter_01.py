import cv2
import numpy as np


def read_img():
    # Read
    img = cv2.imread('open_cv_course_3h/data/lena.png')
    # Show
    cv2.imshow("Output", img)
    # Time to show, if 0 is infitine time. The time it is ms.
    cv2.waitKey(0)
    return


def read_video():
    cap = cv2.VideoCapture('open_cv_course_3h/data/nyc.mp4')
    while True:
        succes, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return


def read_webcam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 100)

    while True:
        succes, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return


img = cv2.imread('open_cv_course_3h/data/lena.png')
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroaded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Eroaded image", imgEroaded)
cv2.waitKey(0)
