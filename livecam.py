import cv2

cap = cv2.VideoCapture(0)
while True:
    frame = cap.read()[1]
    cv2.imshow("camtest", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

