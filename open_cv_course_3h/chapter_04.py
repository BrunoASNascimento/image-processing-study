import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# Change colors
# img[:] = 0, 255, 0  # Color Green
# img[200:300, 100:300] = 255, 0, 0  # Color Blue

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 255, 255), 2)
# cv2.rectangle(img, (0, 0), (250, 350), (0, 255, 255), cv2.FILLED) # Image filled
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

cv2.putText(img, 'OPENCV', (300, 200),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)


cv2.imshow('Image', img)
cv2.waitKey(0)
