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

# Set up the button
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

def convert_number(num, shape):
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
    
    if shape == 'circle':
        shape_utf = ['\u25cb', '\u25c9']
    elif shape == 'rhombus':
        shape_utf = ['\u25c7', '\u25c8']
    elif shape == 'square':
        shape_utf = ['\u25a1', '\u25a3']
        
    num1 = num1.replace('0', shape_utf[0]).replace('1', shape_utf[1])
    num2 = num2.replace('0', shape_utf[0]).replace('1', shape_utf[1])
    return num1, num2

shape_options = itertools.cycle(['rhombus', 'square', 'circle'])
shape = 'circle' # default shape

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    y = top
    t = time.strftime("%m/%d/%Y %I:%M:%S %p")
    
    if buttonB.value and not buttonA.value: # just buttonA pressed, display the time
        draw.text((x, y), t, font=font, fill="#FFFFFF")
    elif buttonA.value and not buttonB.value: # just buttonB pressed, change the shape
        shape = next(shape_options)
    
    # Define the font color for AM and PM times
    fill_am = '#FFA500'
    fill_pm = '#0000FF'
    font_fill = fill_am
    
    # Get the current hour, minute, and second
    hour, minute, second = map(int, time.strftime("%I %M %S").split())
    p = time.strftime("%p") # AM or PM
    
    if p == 'PM':
        font_fill = fill_pm
    
    h1, h2 = convert_number(hour, shape)
    m1, m2 = convert_number(minute, shape)
    s1, s2 = convert_number(second, shape)
    
    for i in range(4):
        y += font.getsize(t)[1]
        text = '   '.join([str(2**(3-i)), h1[i], h2[i], m1[i], m2[i], s1[i], s2[i]])
        draw.text((x, y), text, font=font, fill=font_fill)
        
    # Display image.
    disp.image(image, rotation)
    time.sleep(0.01)
