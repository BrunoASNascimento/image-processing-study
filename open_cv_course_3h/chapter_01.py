import cv2


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
