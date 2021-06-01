import cv2
import tracker
import keyboard
from os import system

def scan(cap, detector, it):
	success, img = cap.read()
	img = detector.findHands(img)
	joints, bbox = detector.findPosition(img)

	system('cls')
	print('ITERATION:', it)
	print('Y:', joints[8][2])
	print('X:', joints[8][1])

	cv2.imshow(f'Joint Detector', img)
	cv2.waitKey(1)
	
	return coords
