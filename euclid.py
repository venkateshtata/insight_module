import sys
import numpy as np
import time
import cv2
import imagezmq
from imutils.video import VideoStream

class euclid_engine(object):
    """docstring for euclid"""
    
    

    def __init__(self, device_name='euclid', ip='localhost',port=5555):
        self.device_name = device_name
        self.port = port
        self.ip = ip
        self.image_hub = imagezmq.ImageHub()
        self.device_id = self.device_name+':'+str(self.ip)
        self.sender = imagezmq.ImageSender(connect_to='tcp://'+ip+':'+str(port))

    def init_web(self):
            self.video_stream = VideoStream(0).start()

    def init_rpi(self):
            self.video_stream = VideoStream(usePiCamera=True).start()

    def send_image(self, width=128, height=128):
        self.height = height
        self.width = width
        self.image = self.video_stream.read()
        self.image=cv2.resize(self.image, (self.width, self.height))
        try:
        	self.sender.send_image(self.device_id, self.image)
        except:
        	print("unable to send")

        return self.device_id

    def recv_image(self):
        self.rpi_name, self.image = self.image_hub.recv_image()
        self.image_hub.send_reply(b'OK')
        return self.rpi_name, self.image



        
