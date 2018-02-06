# DnDSoundboard

Soundboard Created with Raspberry Pi to be used in D&amp;D sessions. 


## Intro

In D&amp;D we often try to find ambient sounds or music that fits in with wherever we are in our campaign. There are times when specific sound effects are needed often (every time a spell is cast, whenever you open a door, whenever someone trips, etc.). The goal of this project is to create something that is ready to play whatever sound is necessary with a quick press of a button. 

## Requirements of the project

+ Portability
+ Ability to assign NUMEROUS sounds
+ Cheap
+ Entertaining

## Hardware used for the soundboard

+ Raspberry Pi 3
+ Momentary push buttons
+ 16x2 LCD Screen
+ Wires
+ Toggle LED Lit Cover Switch (for shutdown?)
+ Empty Wooden Cigar Box (Find a better case?)

LCD Screen used was found on ebay with title

'New Blue IIC I2C TWI 1602 16x2 Serial LCD Module Display for Arduino LAUS'

## Initial Idea of layout

3 rows of 4 push buttons equalling 12 buttons total to play sound on. 

Sounds to be played are determined by what category of sounds you are on which will be determined by a push button to the right of the LCD screen. When pressed, it will change the category of sounds that will be played from and displayed on the LCD screen.
Current category ideas:
+ Ambient
+ Spell effects
+ Voices
+ Combat
+ Bardic Tones

LCD Screen inset in the top of the box so that when a sound is pressed, display the name of the sound file. Also to display what category of sounds you are on.

## Script Requirements

The project uses pygame to play sounds and a fork of a LCD Screen library. Python 3 is also needed for the project.

LCD Screen LIbrary:

'https://github.com/the-raspberry-pi-guy/lcd'

Link to LCD Screen setup tutorial:

'https://www.youtube.com/watch?v=fR5XhHYzUK0'


## Run on Startup

I want this soundboard to start up every time I plug it in no matter where I'm at. So starting the script on startup is a must. To do this, edit your /etc/rc.local

'sudo nano /etc/rc.local'

Then add the following just before the exit 0.

'sudo python /path/to/DnDSoundboard/soundpi.py'

### But What About Shutdown

You'll also need to add the shutdown script. This listens for pressing and holding down the category cycle button. After two seconds of holding it down, it shuts down the pi after halting all tasks. Add it to your rc.local just after the call to run the soundpi.py file.

'sudo python /path/to/DnDSoundboard/shutdown.py'

## Current GPIO Pin Layout

Here are currently the pins being used for the project. Stating buttons starts at top left, moves right, then next row down left, moves right etc.:

| GPIO PIN      | Purpose       |
| ------------- |:-------------:|
| Ground Pin 06 | LCD Ground    |
| GPIO02        | LCD Data      |
| GPIO03        | LCD Data      |
| 5v Pin 02     | LCD Power     |
| GPIO04        | Sfx Button 1  |
| GPIO17        | Sfx Button 2  |
| GPIO27        | Sfx Button 3  |
| GPIO22        | Sfx Button 4  |
| GPIO10        | Sfx Button 5  |
| GPIO09        | Sfx Button 6  |
| GPIO11        | Sfx Button 7  |
| GPIO05        | Sfx Button 8  |
| GPIO06        | Sfx Button 9  |
| GPIO13        | Sfx Button 10 |
| GPIO19        | Sfx Button 11 |
| GPIO26        | Sfx Button 12 |
| GPIO20        | Came undone   |
| GPIO21        | Category cycle|



