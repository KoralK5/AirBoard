import cv2
import tracker
import keyboard
from os import system

def scan(cap, detector):
	success, img = cap.read()
	img = detector.findHands(img)
	joints, bbox = detector.findPosition(img)

	if not len(joints):
		return None, img, bbox

	return joints, img, bbox

def closest(locations, x, y):
	best, curr = 1000, ''
	for row in locations:
		score = abs(x - row[1]) + abs(y - row[2])
		if score <= best:
			best = score
			curr = row[0]

	return curr, best
