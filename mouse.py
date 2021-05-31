import cv2
import tracker
import numpy as np

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = tracker.handDetector(maxHands=1)

while True:
	success, img = cap.read()
	img = detector.findHands(img)

	coords = detector.results.multi_hand_landmarks
	joints, bbox = detector.findPosition(img)
	
	print(len(joints))
	if len(joints) != 0:
		x1, y1 = joints[8][1:]
		x2, y2 = joints[12][1:]
		print(x1, y1, x2, y2)
	
	cv2.imshow("Image", img)
	cv2.waitKey(1)
