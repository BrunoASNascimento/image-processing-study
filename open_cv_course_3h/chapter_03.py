import cv2

img = cv2.imread('open_cv_course_3h/data/lambo.png')
print(img.shape)

imgResize = cv2.resize(img, (300, 200))
imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
