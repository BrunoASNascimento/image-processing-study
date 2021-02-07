import cv2
import numpy as np

width_img, height_img = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)


def pre_processing(img):
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_grey, (5, 5), 1)
    img_canny = cv2.Canny(img_blur, 200, 200)
    kernel = np.ones((5, 5))
    img_dial = cv2.dilate(img_canny, kernel, iterations=2)
    img_thres = cv2.erode(img_dial, kernel, iterations=1)

    return img_thres


def get_contours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biggest = np.array([])
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 5000:
            cv2.drawContours(img_count, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if (area > max_area) and (len(approx) == 4):
                biggest = approx
                max_area = area
    return biggest


while True:
    succes, img = cap.read()
    cv2.resize(img, (width_img, height_img))
    img_count = img.copy()
    img_thres = pre_processing(img)
    get_contours(img_thres)
    cv2.imshow("Result", img_count)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
