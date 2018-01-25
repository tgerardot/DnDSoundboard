import RPi.GPIO as GPIO
import time
import pygame
pygame.mixer.init()


GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

page_number = 0
print (page_number)

if page_number >= 2:
    page_number = 0

while page_number == 0:
    if (GPIO.input(4) == False):
             pygame.mixer.music.load('sounds/misc/airhorn.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(17) == False):
             pygame.mixer.music.load('sounds/misc/alert.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(27) == False):
             pygame.mixer.music.load('sounds/misc/dragon-roar.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(22) == False):
             pygame.mixer.music.load('sounds/misc/glug-glug.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(10) == False):
             pygame.mixer.music.load('sounds/misc/holy.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(9) == False):
             pygame.mixer.music.load('sounds/misc/horn-of-war.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)                                                                 
    if (GPIO.input(11) == False):
             pygame.mixer.music.load('sounds/misc/jump.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(5) == False):
             pygame.mixer.music.load('sounds/misc/phantom.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(6) == False):
             pygame.mixer.music.load('sounds/misc/sneak.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(13) == False):
             pygame.mixer.music.load('sounds/misc/zombie-crowd.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(19) == False):
             pygame.mixer.music.load('sounds/misc/zombie-hit.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(26) == False):
             pygame.mixer.music.load('sounds/misc/zombie-hit.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)                                      

while page_number == 1:
    if (GPIO.input(4) == False):
             pygame.mixer.music.load('sounds/battle/arrow-swoosh-hit.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(17) == False):
             pygame.mixer.music.load('sounds/battle/impale.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(27) == False):
             pygame.mixer.music.load('sounds/battle/slap.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    if (GPIO.input(22) == False):
             pygame.mixer.music.load('sounds/battle/victory.mp3')
             pygame.mixer.music.play(0)
             time.sleep(0.2)
    # if (GPIO.input(10) == False):
    #          pygame.mixer.music.load('sounds/battle/.mp3')
    #          pygame.mixer.music.play(0)
    #          time.sleep(0.2)
    # if (GPIO.input(9) == False):
    #          pygame.mixer.music.load('sounds/battle/.mp3')
    #          pygame.mixer.music.play(0)
    #          time.sleep(0.2)                                                                 
    # if (GPIO.input(11) == False):
    #          pygame.mixer.music.load('sounds/battle/.mp3')
    #          pygame.mixer.music.play(0)
    #          time.sleep(0.2)
    # if (GPIO.input(5) == False):
    #          pygame.mixer.music.load('sounds/battle/.mp3')
    #          pygame.mixer.music.play(0)
    #          time.sleep(0.2)
    # if (GPIO.input(6) == False):
    #          pygame.mixer.music.load('sounds/battle/.mp3')
    #          pygame.mixer.music.play(0)
    #          time.sleep(0.2)
    # if (GPIO.input(13) == False):
    #          pygame.mixer.music.load('sounds/battle/.mp3')
    #          pygame.mixer.music.play(0)
    #          time.sleep(0.2)
    # if (GPIO.input(19) == False):
    #          pygame.mixer.music.load('sounds/battle/.mp3')
    #          pygame.mixer.music.play(0)
    #          time.sleep(0.2)
    # if (GPIO.input(26) == False):
    #          pygame.mixer.music.load('sounds/battle/.mp3')
    #          pygame.mixer.music.play(0)
    #          time.sleep(0.2)
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
