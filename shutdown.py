#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import time
import lcddriver

gpio_pin_number=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    time.sleep(2)
    if GPIO.input(gpio_pin_number) == 0:
        break

os.system("sudo shutdown -h now")