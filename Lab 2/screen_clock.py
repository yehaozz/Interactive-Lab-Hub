import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import itertools

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
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
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
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

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

<<<<<<< HEAD
# Set up the button
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

def convert_number(num, shape):
=======
def convert_number(num):
>>>>>>> cd2c027cc88c671496baed9bee992a4d1b84b010
    """
    Convert the given decimal number to two strings representing two 4-digit binary numbers.
    """
    l = len(str(num)) # number of digits of the decimal number
    if l == 1:
        num1 = '0000'
        num2 = f'{num:04b}' # convert to binary str
    else:
        num1 = f'{int(str(num)[0]):04b}'
        num2 = f'{int(str(num)[1]):04b}'
    
<<<<<<< HEAD
    if shape == 'circle':
        shape_utf = ['\u25cb', '\u25c9']
    elif shape == 'rhombus':
        shape_utf = ['\u25c7', '\u25c8']
    elif shape == 'square':
        shape_utf = ['\u25a1', '\u25a3']
        
    num1 = num1.replace('0', shape_utf[0]).replace('1', shape_utf[1])
    num2 = num2.replace('0', shape_utf[0]).replace('1', shape_utf[1])
=======
    num1 = num1.replace('0', '\u25cb').replace('1', '\u25c9')
    num2 = num2.replace('0', '\u25cb').replace('1', '\u25c9')
>>>>>>> cd2c027cc88c671496baed9bee992a4d1b84b010
    return num1, num2

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    y = top
<<<<<<< HEAD
    t = time.strftime("%m/%d/%Y %I:%M:%S %p")
    
    shape_options = itertools.cycle(['rhombus', 'square', 'circle'])
    shape = 'circle' # default shape
    
    if buttonB.value and not buttonA.value: # just buttonA pressed, display the time
        draw.text((x, y), t, font=font, fill="#FFFFFF")
    elif buttonA.value and not buttonB.value: # just buttonB pressed, change the shape
        shape = next(shape_options)
=======
    t = time.strftime("%m/%d/%Y %H:%M:%S")
    draw.text((x, y), t, font=font, fill="#000000")
>>>>>>> cd2c027cc88c671496baed9bee992a4d1b84b010
    
    # Define the font color for AM and PM times
    fill_am = '#FFA500'
    fill_pm = '#0000FF'
    font_fill = fill_am
    
    # Get the current hour, minute, and second
    hour, minute, second = map(int, time.strftime("%H %M %S").split())
    
    if hour > 12:
        hour -= 12
        font_fill = fill_pm
    
<<<<<<< HEAD
    h1, h2 = convert_number(hour, shape)
    m1, m2 = convert_number(minute, shape)
    s1, s2 = convert_number(second, shape)
=======
    h1, h2 = convert_number(hour)
    m1, m2 = convert_number(minute)
    s1, s2 = convert_number(second)
>>>>>>> cd2c027cc88c671496baed9bee992a4d1b84b010

    y += font.getsize(t)[1]
    text = '   '.join(['8', h1[0], h2[0], m1[0], m2[0], s1[0], s2[0]])
    draw.text((x, y), text, font=font, fill=font_fill)
    
    y += font.getsize(t)[1]
    text = '   '.join(['4', h1[1], h2[1], m1[1], m2[1], s1[1], s2[1]])
    draw.text((x, y), text, font=font, fill=font_fill)
    
    y += font.getsize(t)[1]
    text = '   '.join(['2', h1[2], h2[2], m1[2], m2[2], s1[2], s2[2]])
    draw.text((x, y), text, font=font, fill=font_fill)
    
    y += font.getsize(t)[1]
    text = '   '.join(['1', h1[3], h2[3], m1[3], m2[3], s1[3], s2[3]])
    draw.text((x, y), text, font=font, fill=font_fill)
    
    # Display image.
    disp.image(image, rotation)
<<<<<<< HEAD
    time.sleep(0.01)
=======
    time.sleep(1)

>>>>>>> cd2c027cc88c671496baed9bee992a4d1b84b010
