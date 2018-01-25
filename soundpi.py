import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

page_number = 0
print (page_number)

if page_number >= 2:
    page_number = 0

while page_number == 0:
    if (GPIO.input(18) == False):
             pygame.mixer.music.load('sounds/airhorn.mp3')
			 pygame.mixer.music.play(0)
             page_number += 1
			 time.sleep(0.2)

while page_number == 1:
    if (GPIO.input(18) == False):
             pygame.mixer.music.load('sounds/airhorn.mp3')
			 pygame.mixer.music.play(0)
             time.sleep(0.2)
             if page_number >= 2:
                 page_number = 0



#test
#while True:
#    input_state = GPIO.input(18)
#    if input_state == False:
#        page_number += 1
#        print('Button Pressed')
#        print(page_number)
#        time.sleep(0.2)
