import RPi.GPIO as GPIO
import os
import time
import pygame
pygame.mixer.init()
import lcddriver

display = lcddriver.lcd()

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

category = 0
print (category)


if (GPIO.input(4) == False) and (GPIO.input(17) == False):
    display.lcd_display_string("Powering", 1) 
    display.lcd_display_string("Down....", 1) 
    os.system("sudo shutdown -h now")

while True:
    if (GPIO.input(21) == False):
        category += 1
        time.sleep(0.2)
    if category >= 2:
        category = 0


display.lcd_display_string("Welcome to", 1) 
display.lcd_display_string("D&D SoundPi", 2)
time.sleep(2)                            
display.lcd_clear()    
display.lcd_display_string("Press a Button", 1)

while category == 0:
    if (GPIO.input(4) == False):
             pygame.mixer.music.load('sounds/misc/airhorn.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Airhorn", 2)
             time.sleep(0.2)
    if (GPIO.input(17) == False):
             pygame.mixer.music.load('sounds/misc/alert.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Alert", 2)
             time.sleep(0.2)
    if (GPIO.input(27) == False):
             pygame.mixer.music.load('sounds/misc/dragon-roar.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Dragon Roar", 2)
             time.sleep(0.2)
    if (GPIO.input(22) == False):
             pygame.mixer.music.load('sounds/misc/glug-glug.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Potion Chug", 2)
             time.sleep(0.2)
    if (GPIO.input(10) == False):
             pygame.mixer.music.load('sounds/misc/holy.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Holy Sound", 2)
             time.sleep(0.2)
    if (GPIO.input(9) == False):
             pygame.mixer.music.load('sounds/misc/horn-of-war.mp3')
             pygame.mixer.music.play(0)
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Horn Of War", 2)
             time.sleep(0.2)                                                                 
    if (GPIO.input(11) == False):
             pygame.mixer.music.load('sounds/misc/jump.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Jump", 2)
             time.sleep(0.2)
    if (GPIO.input(5) == False):
             pygame.mixer.music.load('sounds/misc/phantom.mp3')
             pygame.mixer.music.play(0)
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Phantom", 2)
             time.sleep(0.2)
    if (GPIO.input(6) == False):
             pygame.mixer.music.load('sounds/misc/sneak.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Sneak", 2)
             time.sleep(0.2)
    if (GPIO.input(13) == False):
             pygame.mixer.music.load('sounds/misc/zombie-crowd.mp3')
             pygame.mixer.music.play(0)
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Zomb Group", 2)
             time.sleep(0.2)
    if (GPIO.input(19) == False):
             pygame.mixer.music.load('sounds/misc/zombie-hit.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Zombie Hit", 2)
             time.sleep(0.2)
    if (GPIO.input(26) == False):
             pygame.mixer.music.load('sounds/misc/zombie-hit.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Zombie hit?", 2)
             time.sleep(0.2)

while category == 1:
    if (GPIO.input(4) == False):
             pygame.mixer.music.load('sounds/battle/arrow-swoosh-hit.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Arrow Hit", 2)
             time.sleep(0.2)
    if (GPIO.input(17) == False):
             pygame.mixer.music.load('sounds/battle/impale.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Impale", 2)
             time.sleep(0.2)
    if (GPIO.input(27) == False):
             pygame.mixer.music.load('sounds/battle/slap.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Slap", 2)
             time.sleep(0.2)
    if (GPIO.input(22) == False):
             pygame.mixer.music.load('sounds/battle/victory.mp3')
             pygame.mixer.music.play(0)
             display.lcd_clear()
             display.lcd_display_string("Now Playing", 1)
             display.lcd_display_string("Victory!!!!", 2)
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



#test
#while True:
#    input_state = GPIO.input(18)
#    if input_state == False:
#        category += 1
#        print('Button Pressed')
#        print(category)
#        time.sleep(0.2)

