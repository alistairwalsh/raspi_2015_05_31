#!/usr/bin/python

import picamera
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
    