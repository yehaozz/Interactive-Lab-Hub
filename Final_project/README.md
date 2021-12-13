<p align="center">
  <img src="images/Lit_Up.png" height="150"/>
</p>

# Lit Up

_Lit Up_ is a comprehensive system with mood detection, powered by machine learning, music recommendation, and audio visualization. The system recommends music based on the user's mood, and respond to the music's rhythm with LEDs. We hope the user's can lighten up with Lit Up!

## Motivation & Design
Explain why we implement our project. Include our storyboard. Maybe include motto?

The main purpose behind implementing this project was how students, especially towards the end of the semester, would be going through a lot of stress. So this tool would help a student or any person that is busy working on something and is anxious or stressed to lighten up based on how they’re feeling without having to waste time on choosing music by answering if they would like the music to change their mood or accompany it. Things are made more interesting by including a music visualizer LED strip to accompany the music. There is also the option of using just the music visualizer for party purposes without using the emotion detector to control it. This makes the usability of the device very flexible for the user to interact with in different scenarios.

## Features & Demo
What makes our project stand out? (mood detector, visualzier, controller)

**Include _video_ of interaction**

[//]: # (This may be the most platform independent comment)
## Hardware Setup
### Parts Needed
Include a list/table of parts we used. May be better if images are included.

1. Raspberry Pi

    We used Raspberry Pi 4 Model B.

    [<img src="images/RasPi.jpg" height="300">](https://vilros.com/products/raspberry-pi-4-model-b-8gb-ram?src=raspberrypi)

2. LED strip

    We used WS2812B LED strip. This project is also compatible with Adafruit NeoPixel.

    [<img src="images/WS2812B.jpg" height="100">](https://www.amazon.com/gp/product/B01CDTEE5W/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&th=1)

3. Microphone

    We used a USB microphone to capture audio input.
    
    [<img src="images/USB_mic.jpg" height="200">](https://www.amazon.com/SunFounder-Microphone-Raspberry-Recognition-Software/dp/B01KLRBHGM?ref_=ast_sto_dp&th=1&psc=1)

4. Web camera

    We used a web camera to capture user's facial expressions for the mood detection task.
 
    [<img src="images/webcam.jpg" height="250">](https://www.amazon.com/Provision-ISR-Webcam-Microphone-Compatible/dp/B08HL4VFFK)

6. 5V Power Supply

    A 5V AC/DC adaptor was used to supply power for the LED strip.

    [<img src="images/adaptor.jpg" height="300">](https://www.amazon.com/gp/product/B078RXZM4C/ref=ppx_yo_dt_b_asin_image_o03_s01?ie=UTF8&th=1)
 
7. Level shifter
    
    The level shifter was used to shift voltage from 3.3V to 5V.
 
    [<img src="images/level_shifter.jpg" height="200">](https://www.amazon.com/gp/product/B08GJF43N3/ref=ppx_yo_dt_b_asin_image_o03_s00?ie=UTF8&psc=1)

### Raspberry Pi Wiring
Explain how all the parts are wired up with the RasPi

## Dependency Installation
Provide step by step series of examples and explanations about how to get a environment running.

## Configuration & Tests
Describe how to test both hardware and denpendencies are properly set up.

## Let the Interaction Begin
Show how to run the controller, mood detector, audio visualizer.

## Credits
Give proper credits. Cite any repos, blogposts, videos, (people?) that help with our implementation

## Reflections
What have you learned or wish you knew at the start?

Leave it here to remind us that we should submit reflections on Canvas.
