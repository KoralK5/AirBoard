import calibrator as cal
import detector as det
import tracker
import cv2
from os import system

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = tracker.handDetector(maxHands=1)
locations = cal.calibrate(cap, detector, 26)

print('\nKeyboard Coordinates:\n', locations)

n = 0
while True:
	n += 1
	coords = det.scan(cap, detector, n)

	if coords:
		system('cls')
		print('ITERATION:', it)
		print('Y:', coords[8][2])
		print('X:', coords[8][1])

		_, x, y = coords[8]

		# key = det.closest(locations, coords)
