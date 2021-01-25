import cv2


face_cascate = cv2.CascadeClassifier(
    "open_cv_course_3h/data/haarcascades/haarcascade_frontalface_default.xml")
# img = cv2.imread('open_cv_course_3h/data/lena.png')
img = cv2.imread('open_cv_course_3h/data/phantom.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascate.detectMultiScale(img_gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv2.imshow("Result", img)
cv2.waitKey(0)
