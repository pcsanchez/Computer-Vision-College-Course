import cv2
import numpy as np

def create_circle(event, x, y, flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),thickness=10)

img = np.zeros((512,512,3))

cv2.namedWindow(winname='img')

cv2.setMouseCallback('img', create_circle)

while True:

    cv2.imshow('img', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
