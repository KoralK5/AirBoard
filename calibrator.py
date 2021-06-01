import cv2
import tracker
import keyboard
from os import system

def calibrate(cap, detector):
	system('cls')
	print('CALIBRATING...\n\n')
	print('Please center your keyboard under your camera and press every alphabet letter!\n')

	n, coords, prevKey = 0, [], ''
	while len(coords) < 26:
		n += 1
		success, img = cap.read()
		img = detector.findHands(img)
		joints, bbox = detector.findPosition(img)
		if len(joints):
			try:
				key = keyboard.read_key()
				if key != prevKey:
					system('cls')
					print(f'FRAME {n}:\n')
					print(f'{key} at {joints[8]}')
					coords.append((key, joints[8][1], joints[8][2]))
				prevKey = key
			except:
				pass
			
		cv2.imshow(f'Joint Detector', img)
		cv2.waitKey(1)
		
	system('cls')
	print('Calibration Sucessfull!')
	return coords
