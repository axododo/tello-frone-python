import keyboard
from djitellopy import Tello
import time
import cv2
import numpy as np

drone = Tello()

drone.connect()

turn_left = 0
monter = 0
avancer = 0
left = 0

while True:
    if keyboard.wait('z')
        avancer = 50
    elif keyboard.wait('s')
        avancer = -50
    elif keyboard.wait('q')
        left = 50
    elif keybord.wait('')
