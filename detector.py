import cv2
import tracker
import keyboard
from os import system

def scan(cap, detector, it):
	success, img = cap.read()
	img = detector.findHands(img)
	joints, bbox = detector.findPosition(img)

	cv2.imshow(f'Joint Detector', img)
	cv2.waitKey(1)

	if not len(joints):
		return None

	return joints

def closest(locations, coords):
	return None
