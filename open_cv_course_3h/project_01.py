import cv2
import numpy as np
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 350)

my_colors = [
    [56, 255, 67,  126,  255, 255, 'Green'],
    [56, 202, 214, 179,  255, 255, 'Red']
]
my_colors_values = [[0, 255, 0], [0, 0, 255]]
my_points = []  # [x,y,colorId]


def find_color(img, my_colors, my_colors_values):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    new_points = []
    for idx, color in enumerate(my_colors):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(img_hsv, lower, upper)
        x, y = get_contours(mask)
        cv2.circle(img_result, (x, y), 5, my_colors_values[idx], cv2.FILLED)
        if x != 0 and y != 0:
            new_points.append([x, y, idx])
    return new_points
    # cv2.imshow(color[6], mask)


def get_contours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(img_result, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y


def draw_on_canvas(my_points, my_color_values):
    for point in my_points:
        cv2.circle(img_result, (point[0], point[1]),
                   10, my_color_values[point[2]], cv2.FILLED)


while True:
    succes, img = cap.read()
    img_result = img.copy()
    new_points = find_color(img, my_colors, my_colors_values)
    if len(new_points) != 0:
        for new_point in new_points:
            my_points.append(new_point)
    if len(my_points) != 0:
        draw_on_canvas(my_points, my_colors_values)
    cv2.imshow("Result", img_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
