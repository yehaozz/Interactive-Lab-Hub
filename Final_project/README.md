<p align="center">
  <img src="images/Lit_Up.png" height="150"/>
</p>

# Lit Up

_Lit Up_ is a comprehensive system with mood detection, powered by machine learning, music recommendation, and audio visualization. The system recommends music based on the user's mood, and respond to the music's rhythm with LEDs. We hope the user's mood can lighten up with Lit Up!

## Motivation & Design

<p align="center">
  <em>"We breathe the light, we breathe the music, we breathe the moment as it passes through us." <strong>— Anne Rice</strong></em>
</p>

The main purpose behind implementing this project was how students, especially towards the end of the semester, would be going through a lot of stress. We believe a simple combination of light and music can trigger inner peace and joy. So our system would help a student or any person that is busy working on something and is anxious or stressed to lighten up based on how they’re feeling without having to waste time on choosing music by answering if they would like the music to change their mood or accompany it. Things are made more interesting by including a music visualizer LED strip to accompany the music. There is also the option of using just the music visualizer for party purposes without using the emotion detector to control it. This makes the usability of the device very flexible for the user to interact with in different scenarios.

### Structure

<img src="images/structure.png" height=200>

### Storyboard

<img src="images/storyboard.png" height=300>

## Features & Demo
What makes our project stand out? (mood detector, visualzier, controller)

There are three key components in Lit Up.

- Mood detection

  The system can detect the moods of users, such as happy and sad. And based on the detection results, the system can recommend corresponding music to users to cheer them up.


- Audio visualization

  The LED strip can interact with the music. Based on the rhythm and strength of the music, the color and the flicker frequency of each LED spot will change accordingly. And spots on the LED strip can show different performances as a whole according to the music pieces.

- Controller

  We have a controller platform, where it can capture the user’s facial expression to detect his/her mood. And there are different kinds of music on the platform, based on the detection result, the system can recommend music to the user to cheer him/her up. The user can speak to interact with the platform, and the platform can respond with voices.

**Include _video_ of interaction**

[//]: # (Videos need to be edited.)

## Hardware Setup
### Parts Needed

1. Raspberry Pi

   We used Raspberry Pi 4 Model B.

   [<img src="images/RasPi.jpg" height=200>](https://vilros.com/products/raspberry-pi-4-model-b-8gb-ram?src=raspberrypi)

2. LED strip

   We used WS2812B LED strip. This project is also compatible with Adafruit NeoPixel.

   [<img src="images/WS2812B.jpg" height=90>](https://www.amazon.com/gp/product/B01CDTEE5W/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&th=1)

3. Microphone

   We used a USB microphone to capture audio input.
    
   [<img src="images/USB_mic.jpg" height=150>](https://www.amazon.com/SunFounder-Microphone-Raspberry-Recognition-Software/dp/B01KLRBHGM?ref_=ast_sto_dp&th=1&psc=1)

4. Web camera

   We used a web camera to capture user's facial expressions for the mood detection task.
 
   [<img src="images/webcam.jpg" height=200>](https://www.amazon.com/Provision-ISR-Webcam-Microphone-Compatible/dp/B08HL4VFFK)

6. 5V Power Supply

   A 5V AC/DC adaptor was used to supply power for the LED strip.

   [<img src="images/adaptor.jpg" height=250>](https://www.amazon.com/gp/product/B078RXZM4C/ref=ppx_yo_dt_b_asin_image_o03_s01?ie=UTF8&th=1)
 
7. Level shifter
    
   The level shifter was used to shift voltage from 3.3V to 5V.
 
   [<img src="images/level_shifter.jpg" height=150>](https://www.amazon.com/gp/product/B08GJF43N3/ref=ppx_yo_dt_b_asin_image_o03_s00?ie=UTF8&psc=1)

### Raspberry Pi Wiring

1. Connect the webcam and the USB microphone to the Raspberry Pi.
2. Wire the LED strip with the Raspberry Pi.
   
   We followed the digram below for the wiring.
   
   <img src=https://cdn-learn.adafruit.com/assets/assets/000/064/121/original/led_strips_raspi_NeoPixel_Level_Shifted_bb.jpg?1540314807, height=300>
   
   Alternative ways to wire Raspberry Pi with the LED strip can be found in this [tutorial](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring).

## Dependency Installation
Provide step by step series of examples and explanations about how to get a environment running.

### Connect to your Pi and create a virtual environment

```
ssh pi@<your Pi's IP address>
...
pi@ixe00:~ $ virtualenv led_strip
pi@ixe00:~ $ source led_strip/bin/activate
(led_strip) pi@ixe00:~ $ 
```

### Clone the repository and install requirements 

```
(led_strip) pi@ixe00:~$ git clone https://github.com/yehaozz/Interactive-Lab-Hub.git
(led_strip) pi@ixe00:~$ cd Interactive-Lab-Hub/Final_project/
(led_strip) pi@ixe00:~/Interactive-Lab-Hub/Final_project $ ./install_tensorflow.sh
(led_strip) pi@ixe00:~/Interactive-Lab-Hub/Final_project $ pip install -r requirements.txt
```

There might be compatibility issues, most of which can be solved by searching the error message (google, stack overflow). 

## Configuration & Tests
Describe how to test both hardware and denpendencies are properly set up.

### Configuration

In [config.py](config.py):

- Set N_PIXELS to the number of LEDs in your LED strip.
- Set ORDER to match the color ordering of the LED strip. The color channel order is either “RGB” or “GRB”.

We also set other default configurations in the [config.py](config.py) script. The default settings should work fine if following the above mentioned steps. But these settings are also customizable. Feel free to modify them to suit your needs.

### Test the mood detection and the controller

To use the plain camera as input to the controller, uncomment the line 12 in [app.py](app.py) and comment out the line 13.  

```
12	# Camera = import_module('camera.camera_opencv').Camera
13	Camera = import_module('camera.camera_teachable_machine').Camera
14	camera = Camera()
```

Then run  

```
(led_strip) pi@ixe00:~/Interactive-Lab-Hub/Final_project $ python app.py
```

The video feeds should be displayed on the controller. By changing the Camera module chosen in [app.py](app.py), you can change the video processing pipeline and extract different information. 


## Let the Interaction Begin
Show how to run the controller, mood detector, audio visualizer.

Open a terminal window, and run

```
(led_strip) pi@ixe00:~/Interactive-Lab-Hub/Final_project $ python app.py
```


In a separate terminal, run the following command to get the system ready for visualization.
```
(led_strip) pi@ixe00:~/Interactive-Lab-Hub/Final_project $ sudo  python visualization.py
```

## Credits
Give proper credits. Cite any repos, blogposts, videos, (people?) that help with our implementation
