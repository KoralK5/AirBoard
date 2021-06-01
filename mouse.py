import cv2
import tracker
import numpy as np
from os import system

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = tracker.handDetector(maxHands=1)

system('cls')
while True:
	success, img = cap.read()
	img = detector.findHands(img)

	coords = detector.results.multi_hand_landmarks
	joints, bbox = detector.findPosition(img)
	
	if len(joints) != 0:
		system('cls')
		print('Joints:\n', np.array(joints))
	
	cv2.imshow("Image", img)
	cv2.waitKey(1)
