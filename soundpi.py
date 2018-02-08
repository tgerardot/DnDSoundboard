#!/usr/bin/python

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

display.lcd_display_string("Welcome to", 1) 
display.lcd_display_string("D&D SoundPi", 2)
time.sleep(2)                            
display.lcd_clear()    
display.lcd_display_string("Press a Button", 1)

while True:    
    if category >= 5:
        category = 0
        
    while category == 0:
        if (GPIO.input(21) == False):
                 category += 1
                 display.lcd_clear()
                 display.lcd_display_string("Category Now", 1)
                 display.lcd_display_string("Battle Sounds", 2)
                 time.sleep(0.2)
        if (GPIO.input(4) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/airhorn.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Airhorn", 2)
                 time.sleep(0.2)
        if (GPIO.input(17) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/alert.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Alert", 2)
                 time.sleep(0.2)
        if (GPIO.input(27) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/dragon-roar.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Dragon Roar", 2)
                 time.sleep(0.2)
        if (GPIO.input(22) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/glug-glug.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Potion Chug", 2)
                 time.sleep(0.2)
        if (GPIO.input(10) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/holy.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Holy Sound", 2)
                 time.sleep(0.2)
        if (GPIO.input(9) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/horn-of-war.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Horn Of War", 2)
                 time.sleep(0.2)                                                                 
        if (GPIO.input(11) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/jump.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Jump", 2)
                 time.sleep(0.2)
        if (GPIO.input(5) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/phantom.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Phantom", 2)
                 time.sleep(0.2)
        if (GPIO.input(6) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/sneak.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Sneak", 2)
                 time.sleep(0.2)
        if (GPIO.input(13) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/zombie-crowd.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Zomb Group", 2)
                 time.sleep(0.2)
#        if (GPIO.input(19) == False):
#                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/zombie-hit.mp3')
#                 pygame.mixer.music.play(0)
#                 display.lcd_clear()
#                 display.lcd_display_string("Now Playing", 1)
#                 display.lcd_display_string("Zombie Hit", 2)
#                 time.sleep(0.2)
#        if (GPIO.input(26) == False):
#                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/misc/zombie-hit.mp3')
#                 pygame.mixer.music.play(0)
#                 display.lcd_clear()
#                 display.lcd_display_string("Now Playing", 1)
#                 display.lcd_display_string("Zombie hit?", 2)
#                 time.sleep(0.2)

    while category == 1:
        if (GPIO.input(21) == False):
                 category += 1
                 display.lcd_clear()
                 display.lcd_display_string("Category Now", 1)
                 display.lcd_display_string("Spells", 2)
                 time.sleep(0.2)
        if (GPIO.input(4) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/arrow-swoosh-hit.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Arrow Swoosh Hit", 2)
                 time.sleep(0.2)
        if (GPIO.input(17) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/bow_single_shot.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Bow Shot", 2)
                 time.sleep(0.2)
        if (GPIO.input(27) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/club_attack.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Club Attack", 2)
                 time.sleep(0.2)
        if (GPIO.input(22) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/impale.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Bloody Impale", 2)
                 time.sleep(0.2)
        if (GPIO.input(10) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/large_group.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Large Battle", 2)
                 time.sleep(0.2)
        if (GPIO.input(9) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/punch_x4.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Four Punches", 2)
                 time.sleep(0.2)                                                                 
        if (GPIO.input(11) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/shield_bash.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Shield Bash", 2)
                 time.sleep(0.2)
        if (GPIO.input(5) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/skirmish.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Skirmish", 2)
                 time.sleep(0.2)
        if (GPIO.input(6) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/slap.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Slap", 2)
                 time.sleep(0.2)
        if (GPIO.input(13) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/staff_attack.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Quarterstaff", 2)
                 time.sleep(0.2)
        if (GPIO.input(19) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/sword_hit_3x.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("3 Sword Hits", 2)
                 time.sleep(0.2)
        if (GPIO.input(26) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/battle/victory.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Victory!!!!", 2)
                 time.sleep(0.2)

    while category == 2:
        if (GPIO.input(21) == False):
                 category += 1
                 display.lcd_clear()
                 display.lcd_display_string("Category Now", 1)
                 display.lcd_display_string("Wows", 2)
                 time.sleep(0.2)
        if (GPIO.input(4) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/acid-splash.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Acid Splash", 2)
                 time.sleep(0.2)
        if (GPIO.input(17) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/conjuring.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Conjuring", 2)
                 time.sleep(0.2)
        if (GPIO.input(27) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/earth_spell.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Earth Spell", 2)
                 time.sleep(0.2)
        if (GPIO.input(22) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/fire_spell_2.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Fire Spell", 2)
                 time.sleep(0.2)
        if (GPIO.input(10) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/fireball.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Fireball", 2)
                 time.sleep(0.2)
        if (GPIO.input(9) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/heal_spell_1a.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Heal Spell", 2)
                 time.sleep(0.2)                                                                 
        if (GPIO.input(11) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/ice_spell_2.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Ice Spell", 2)
                 time.sleep(0.2)
        if (GPIO.input(5) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/music_spell_2.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Music Spell", 2)
                 time.sleep(0.2)
        if (GPIO.input(6) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/nature_spell.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Nature Spell", 2)
                 time.sleep(0.2)
        if (GPIO.input(13) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/poison-cloud.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Poison Cloud", 2)
                 time.sleep(0.2)
        if (GPIO.input(19) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/spell_1.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Generic Spell", 2)
                 time.sleep(0.2)
        if (GPIO.input(26) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/spells/thunderwave.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Casting", 1)
                 display.lcd_display_string("Thunderwave", 2)
                 time.sleep(0.2)

    while category == 3:
        if (GPIO.input(21) == False):
                 category += 1
                 display.lcd_clear()
                 display.lcd_display_string("Category Now", 1)
                 display.lcd_display_string("Farts", 2)
                 time.sleep(0.2)
        if (GPIO.input(4) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-1.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow1", 2)
                 time.sleep(0.2)
        if (GPIO.input(17) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-2.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow2", 2)
                 time.sleep(0.2)
        if (GPIO.input(27) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-3.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow3", 2)
                 time.sleep(0.2)
        if (GPIO.input(22) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-4.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow4", 2)
                 time.sleep(0.2)
        if (GPIO.input(10) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-5.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow5", 2)
                 time.sleep(0.2)
        if (GPIO.input(9) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-6.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow6", 2)
                 time.sleep(0.2)                                                                 
        if (GPIO.input(11) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-7.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow7", 2)
                 time.sleep(0.2)
        if (GPIO.input(5) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-8.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow8", 2)
                 time.sleep(0.2)
        if (GPIO.input(6) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-9.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow9", 2)
                 time.sleep(0.2)
        if (GPIO.input(13) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-10.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow10", 2)
                 time.sleep(0.2)
        if (GPIO.input(19) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-11.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow11", 2)
                 time.sleep(0.2)
        if (GPIO.input(26) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/wow/wow-12.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Owen Says", 1)
                 display.lcd_display_string("Wow12", 2)
                 time.sleep(0.2)

    while category == 4:
        if (GPIO.input(21) == False):
                 category += 1
                 display.lcd_clear()
                 display.lcd_display_string("Category Now", 1)
                 display.lcd_display_string("General", 2)
                 time.sleep(0.2)
        if (GPIO.input(4) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/farts/fart-1.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Fart1", 2)
                 time.sleep(0.2)
        if (GPIO.input(17) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/farts/fart-2.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Fart2", 2)
                 time.sleep(0.2)
        if (GPIO.input(27) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/farts/fart-3.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Fart3", 2)
                 time.sleep(0.2)
        if (GPIO.input(22) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/farts/fart-4.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Fart4", 2)
                 time.sleep(0.2)
        if (GPIO.input(10) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/farts/fart-5.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Fart5", 2)
                 time.sleep(0.2)
        if (GPIO.input(9) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/farts/fart-6.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Fart6", 2)
                 time.sleep(0.2)                                                                 
        if (GPIO.input(11) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/farts/fart-7.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Fart7", 2)
                 time.sleep(0.2)
        if (GPIO.input(5) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/farts/fart-8.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Fart8", 2)
                 time.sleep(0.2)
        if (GPIO.input(6) == False):
                 pygame.mixer.music.load('/home/DnDSoundboard/sounds/farts/fart-9.mp3')
                 pygame.mixer.music.play(0)
                 display.lcd_clear()
                 display.lcd_display_string("Now Playing", 1)
                 display.lcd_display_string("Fart9", 2)
                 time.sleep(0.2)
        # if (GPIO.input(13) == False):
        # if (GPIO.input(19) == False):
        # if (GPIO.input(26) == False):
        


