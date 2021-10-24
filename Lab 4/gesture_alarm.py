# imports
import time
from random import randint
import board
import busio
from i2c_button import I2C_Button
from adafruit_servokit import ServoKit
from gtts import gTTS
import os

# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo = kit.servo[2]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo.set_pulse_width_range(500, 2500)

# initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

#================== Gesture ==================#
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE

#================== miniPiTFT ==================#
import digitalio
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors
from PIL import Image, ImageDraw, ImageFont

# The display uses a communication protocol called SPI.
# SPI will not be covered in depth in this course. 
# you can read more https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = display.width  # we swap height/width to rotate it to landscape!
width = display.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
display.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

##############################################################

correct_gestures = ['left', 'up', 'right', 'down']
gesture_to_sensor = {'up':0x01, 'down':0x02, 'left':0x03, 'right':0x04}

def display_info(bgc, rm=None):
    """
    Display info on the screen with background color bgc
    """
    draw.rectangle((0, 0, width, height), outline=0, fill=bgc)
    time_string = time.strftime("%m/%d/%Y %I:%M:%S %p")
    dx, dy = font.getsize(time_string)
    x = (width - dx) / 2
    y = (height - dy) / 2
    if rm:
        step_string = f'Remaining gestures: {rm}'
        draw.text((x, y-dy/2), time_string, font=font, fill="#FFFFFF")
        draw.text((x, y+dy/2), step_string, font=font, fill="#FFFFFF")
    else:
        draw.text((x, y), time_string, font=font, fill="#FFFFFF")    
    
    display.image(image, rotation)

# Initialize rm
rm = int(time.strftime("%I"))

while True and rm != 0:
    try:
        display_info((0,0,0), rm)
        
        gesture_ind = randint(1, 4)
        servo.angle = 45 * gesture_ind
        
        correct_gesture = correct_gestures[gesture_ind - 1]
        
        start = time.time()         # the variable that holds the starting time
        elapsed = 0                 # the variable that holds the number of seconds elapsed.
        
        while elapsed < 10:         # while less than 10 seconds have elapsed  
            
            display_info((0, 0, 0), rm)
            
            sensor_gesture = apds.gesture()
            
            if gesture_to_sensor[correct_gesture] == sensor_gesture:
                
                display_info("#008148", rm)
                # myobj = gTTS(text='correct', lang='en', slow=False)
                # if not os.path.exists('correct.mp3'):
                #     myobj.save('correct.mp3')
                # os.system('mpg321 correct.mp3')
                os.system('mpg321 ./Sound/correct.mp3')
                rm = rm - 1
                if rm == 0:
                    display_info("#008148", '0')
                    os.system('mpg321 ./Sound/gta.mp3')
                break
            elif sensor_gesture:
                display_info((255, 0, 0), rm)
                # myobj = gTTS(text='wrong', lang='en', slow=False)
                # if not os.path.exists('wrong.mp3'):
                #     myobj.save('wrong.mp3')
                # os.system('mpg321 wrong.mp3')
                os.system('mpg321 ./Sound/Negative-sound-effect.mp3')          

            elapsed = time.time() - start #update the time elapsed
        
        # Set the servo to 0 degree position
        servo.angle = 0
        time.sleep(1)
        
    except KeyboardInterrupt:
        # Once interrupted, set the servo back to 0 degree position
        servo.angle = 0
        time.sleep(0.5)
        break

while True:
    display_info("#008148")