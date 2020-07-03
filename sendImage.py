from euclid import euclid_engine
import time
image_stream = euclid_engine("Euclid-RPI", "192.168.225.50")
image_stream.init_rpi()
time.sleep(2)

while True:
	time.sleep(0.01)
	id = image_stream.send_image()