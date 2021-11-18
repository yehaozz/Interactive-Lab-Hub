import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import paho.mqtt.client as mqtt
import uuid

import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import itertools

################################
wCam, hCam = 640, 480
################################
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
 
detector = htm.handDetector(detectionCon=0.7)

COLOR = (204, 153, 102) # blue color
xloc = 40

################ Screen ###################
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

BAUDRATE = 64000000

spi = board.SPI()

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

height = disp.width
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

padding = -2
top = padding
bottom = height - padding

x = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
#######################################################

################ MQTT ################
pth = 'IDD/rspgame/#'
player_no = cmd = input('>> player 1/2: \n')
topic = f'IDD/rspgame/player{player_no}'

player_1_gesture = 0
player_2_gesture = 0

def on_connect(client, userdata, flags, rc):
	# print(f"connected with result code {rc}")
	client.subscribe(pth)

# this is the callback that gets called each time a message is recived
def on_message(cleint, userdata, msg):
    # start = time.time()
    global player_1_gesture
    global player_2_gesture
    global font
    if msg.topic == 'IDD/rspgame/player1':
        # print(f"player 1: {msg.payload.decode('UTF-8')}, retained: {msg.retain}")
        player_1_gesture = msg.payload.decode('UTF-8')
        
    if msg.topic == 'IDD/rspgame/player2':
        # print(f"player 2: {msg.payload.decode('UTF-8')}, retained: {msg.retain}")
        player_2_gesture = msg.payload.decode('UTF-8')
    
    if player_1_gesture and player_2_gesture:
        result = ''
        if player_1_gesture == player_2_gesture:
            result = 'tie'
        elif player_1_gesture == 'rock':
            result = 'player 1 wins' if player_2_gesture == 'scissor' else 'player 2 wins'
        elif player_1_gesture == 'scissor':
            result = 'player 1 wins' if player_2_gesture == 'paper' else 'player 2 wins'
        elif player_1_gesture == 'paper':
            result = 'player 1 wins' if player_2_gesture == 'rock' else 'player 2 wins'
            
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        text = f'player 1: {player_1_gesture}\nplayer 2: {player_2_gesture}\n\n{result}!'
        draw.text((1, -2), text, font=font, fill='#FFFFFF')
        disp.image(image, rotation)
    
    # end = time.time()
    # print(f'elapsed time: {end - start}')

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_start()

# this lets us exit gracefully (close the connection to the broker)
def handler(signum, frame):
    print('exit gracefully')
    client.loop_stop()
    exit (0)
###########################################

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        # coordinate for 5 fingers
        thumbX, thumbY = lmList[4][1], lmList[4][2] #thumb
        pointerX, pointerY = lmList[8][1], lmList[8][2] #pointer
        middleX, middleY = lmList[12][1], lmList[12][2]
        ringX, ringY = lmList[16][1], lmList[16][2]
        pinkyX, pinkyY = lmList[20][1], lmList[20][2]
  
        # draw circle at the end of each finger
        cv2.circle(img, (thumbX, thumbY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (pointerX, pointerY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (middleX, middleY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (ringX, ringY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (pinkyX, pinkyY), 15, (255, 0, 255), cv2.FILLED)

        # calculate the distances for condition
        len_calc = lambda x1,y1,x2,y2: math.hypot(x2 - x1, y2 - y1)
        thumb2ring = len_calc(thumbX,thumbY,ringX,ringY)
        thumb2pinky = len_calc(thumbX,thumbY,pinkyX,pinkyY)
        thumb2pointer = len_calc(thumbX,thumbY,pointerX,pointerY)
        thumb2middle = len_calc(thumbX,thumbY,middleX,middleY)
        pointer2middle = len_calc(pointerX,pointerY,middleX,middleY)
        middle2ring = len_calc(middleX,middleY,ringX, ringY)
        
        # conditions 
        thumb_ring_pinky_close = thumb2ring < 80 and thumb2pinky < 80
        pointer_middle_ring_close = pointer2middle < 80 and middle2ring < 80

        middle_pointer_away_from_thumb = thumb2pointer > 100 and thumb2middle > 100
        ring_pinky_away_from_thumb = thumb2ring > 100 and thumb2pinky > 100

        # condition for 'scissor' gesture
        scissors_condition = thumb_ring_pinky_close and middle_pointer_away_from_thumb 

        # condition for 'rock' gesture
        rock_condition = thumb_ring_pinky_close and pointer_middle_ring_close
        
        # condition for 'paper' gesture
        paper_condition = middle_pointer_away_from_thumb and ring_pinky_away_from_thumb
        
        if rock_condition:
            cv2.putText(img, 'rock', (xloc, 90), cv2.FONT_HERSHEY_COMPLEX,
                1, COLOR, 3)
            client.publish(topic, 'rock')
        elif scissors_condition:
            cv2.putText(img, 'scissor', (xloc, 90), cv2.FONT_HERSHEY_COMPLEX,
                1, COLOR, 3)
            client.publish(topic, 'scissor')
        elif paper_condition:
            cv2.putText(img, 'paper', (xloc, 90), cv2.FONT_HERSHEY_COMPLEX,
                1, COLOR, 3)
            client.publish(topic, 'paper')
        # return None
        
    # Get the frame per second
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
 
    cv2.imshow("Img", img)
    cv2.waitKey(1)