import calibrator as cal
import detector as det
import tracker
import cv2
from os import system
from time import time

amount = int(input('Amount of keys to use: '))

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = tracker.handDetector(maxHands=1)
locations = cal.calibrate(cap, detector, amount)

prevKey, start = '', time()
while True:
	coords, img, bbox = det.scan(cap, detector)

	if coords:
		_, x, y = coords[8]
		key, best = det.closest(locations, x, y)

		xmin, ymin, xmax, ymax = bbox

		if prevKey != key:
			start = time()

		if time() - start > 1:
			cv2.putText(img, key.upper(), ((xmin+xmax)//2, ymin-50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 2, cv2.LINE_AA)
			cv2.rectangle(img, (xmin-20, ymin-20), (xmax+20, ymax+20), (0,255,255), 2)

		else:
			cv2.putText(img, key.upper(), ((xmin+xmax)//2, ymin-50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2, cv2.LINE_AA)
		
		prevKey = key

	cv2.imshow(f'Keypress Detector', img)
	cv2.waitKey(1)
