import cv2
import numpy as np


def manipulations():
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

    return
