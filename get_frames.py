from euclid import euclid_engine
import time
import cv2

eu = euclid_engine()

while True:
	ip, frame = eu.recv_image()
	cv2.imshow('frame',frame)
	cv2.waitKey(1)
cv2.destroyAllWindows()
	