import calibrator as cal
import detector as det
import tracker
import cv2
from os import system

amount = int(input('Amount of keys to use: '))

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = tracker.handDetector(maxHands=1)
locations = cal.calibrate(cap, detector, amount)

n = 0
while True:
	n += 1
	coords = det.scan(cap, detector, n)

	if coords:
		_, x, y = coords[8]

		key, best = det.closest(locations, x, y)

		system('cls')
		print('ITERATION:', n)
		print('\nKey:', key)
		print(f'\nCertainty: {100 - best}%')
