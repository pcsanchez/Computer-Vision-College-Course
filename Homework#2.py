import numpy as np
import cv2

def filter_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_color = hsv[y, x, :]
        param[0][:3] = [max(clicked_color[0] - 15, 0), 100, 100]
        param[1][:3] = [min(clicked_color[0] + 15, 360), 255, 255]
        # print('Clicked:', clicked_color)
        # print('Lower:', param[0])
        
cap = cv2.VideoCapture(0)

_, frame = cap.read()

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(frame, 'Francisco Sanchez', (330, 30), font, 1, (255, 255, 255),2, cv2.LINE_AA)
cv2.putText(frame, 'A01196903', (450, 70), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('frame', frame)
cv2.waitKey(0) & 0xFF

cv2.destroyAllWindows()

lower_bound = np.array([0, 0, 0])
upper_bound = np.array([255, 255, 255])

kernel = np.ones((5, 5), np.uint8)

cv2.namedWindow('video')
cv2.setMouseCallback('video', filter_color, [lower_bound, upper_bound])


while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    res2 = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
    
    cv2.imshow('video', res2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()