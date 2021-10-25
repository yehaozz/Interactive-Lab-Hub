# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### (Optional) Distance Sensor

Note: We did not distribute this sensor to you, so if you are interested in playing with it, please come pick it up from the TA!

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

1. Gesture - an alarm that needs users to make gestures followed by random instructions to turn off, so that it makes sure users wake up

<img src="./images/sketch1.jpg" height="300">

2. Capacitive Sensing - piano or make different sounds when touching different pads

<img src="./images/sketch2.jpg" height="500">

3. Proximity and distance sensor - covid, social distancing, reminding if too close to other people

<img src="./images/sketch3.jpg" height="500">

4. Proximity sensor - greeting, automatically greeting users when they are back home or customers entering a store

<img src="./images/sketch4.png" height="500">

5. Light sensor- seeing the environment light and reducing the light brightness

<img src="./images/sketch5.jpg" height="300">

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

1. Gesture - an alarm that needs users to make gestures followed by random instructions to turn off, so that it makes sure users wake up

   * Questions:
       * The gesture sensor only detects gestures near to it, so that the user has to wave hands right in front of the alarm.
       * The speaker might not be loud enough to wake users up.

   * Solutions:
       * We can make both the gesture sensor and the speaker exposed to the outside of the box, so that it’s easier to detect users’ gestures and the sounds can be louder.

2. Capacitive Sensing - piano or make different sounds when touching different pads

   * The speaking command from the previous lab has some delay, which can make the piano not as interactive. How will the delay affect the user interaction needs a prototype to answer. 
   * The piano keys are connected to the capacitive sensors, so the user can simply touch the keys instead of pressing them. How the connection would work and will user be comfortable with the new way needs prototyping.
   * The width and the length of each piano keys needs prototype to optimize .

3. Proximity and distance sensor - covid, social distancing, reminding if too close to other people
   * The speaker available is from the webcam. That is too huge for a pocket device. 
   * Also the field of sensing for the distance sensor is 25 degrees. If a person is not in this field of view they might not be detected. So prototyping is necessary to understand the limitations of the sensor and how the user will interact with it.
   * Since the device is used in social settings where multiple people are gathered, how other people interact with the device is also necessary to understand the modality of the output to make it cautious as well as non intrusive.

4. Proximity sensor - greeting, automatically greeting users when they are back home or customers entering a store
   * The OLED screen may not be necessary in that the user will be too far from the device to actually read the words on the screen. Physical prototypes are required to examine this question.
   * The proximity sensor should be placed close enough to the door to detect the motion. It might be better using the distance sensor instead.

5. Light sensor- seeing the environment light and reducing the light brightness
   * The screen is not large enough and its light is not bright enough to use as a lamp for the whole room. In this case, we can use the lamp just for a small desk lamp.

**\*\*\*Pick one of these designs to prototype.\*\*\***

We choose the first design, the gesture alarm, to prototype.

### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

1. Use a button to snooze for 10 more minutes after the alarm rings. When the alarm rings, the user can press the side button twice to snooze the alarm and delay the alarm time 10 minutes later.

<img src="./images/display1.png" height="300">

2. Using the OLED display to show both the time and the feedback to the user for the gesture. The entire unit is housed in the cardboard box which includes the pi place at the bottom, gesture sensor right below the display and the speaker from the webcam at the top.

<img src="./images/display2.jpg" height="300">

3. Use two OLED screens. One of the OLED screens is placed next to the user to display the time, while the other is placed in front of the user to show the gesture instructions. The gesture sensor is in front of the user.

<img src="./images/display3.png" height="300">

4. Use two OLED screens. Both of the OLED screens are placed in front of the user, displaying the time and the gesture instructions separately. The gesture sensor is in front of the user.

<img src="./images/display4.png" height="300">

5. Use two OLED screens. They are on two different sides of the device, and displaying the time and the gesture instructions separately. The gesture sensor is next to the user.

<img src="./images/display5.png" height="300">

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

1. Use a button to snooze for 10 more minutes after the alarm rings. The button might be small, and if we embed it into the alarm, it might not be easy for users to press. The solution could be to place the button exposure outside the alarm box so that it will be easier to press.
2. The size of the display might make it hard for the user to read what's on the screen, be it the time or the gesture directions and feedback. Also if the clock is not placed close to the user, the proximity sensor might not be able to sense the gestures the user is showing. The solution for this is to place the entire unit close to the user or to display the time and gesture feedback in different screens and place the gesture sensor closer to the user.
3. Using different modules that are placed far away from each other for the gesture and clock is hard for making the connections since we’re using one Pi to control all the modules.
4. The layout of two screens might constrain the height of the device. Same as sketch 3, the gesture sensor is far from the user which could make it hard for the sensor to pick up the user’s input.
5. To see both the screens in side by side settings, the user needs to be at certain angles to the device. How we want to set up the two screens and what information to display on the displays needs prototyping. 

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

We choose to combine the 4th and 5th design, using two OLED screens and the gesture sensor placed on top of the device. Both of the OLED screens are placed in next to the user, displaying the time and the gesture instructions separately on the same side of the device.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The reason we choose to combine design 4&5 is that showing both the time and the gesture instructions on the side lets the user see both information, which makes more sense in practice. Considering the working distance of the gesture sensor, placing it near the user makes picking up the user's inputs possible. Besides, because the speaker is closer to the user, it should be easier to wake up the user with the same sound volume.

Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***

<img src="./images/prototype1.jpg" height="400">

<img src="./images/prototype2.jpg" height="400">

LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which we will be distributing the battery packs in the class. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.15752-9/245605956_303690921194525_3309212261588023460_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=FvFLlClTKuUAX9nJ3LR&_nc_ht=scontent-lga3-1.xx&oh=b7ec1abc8d458b6c1b7a00a6f11398ac&oe=618D7D96" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Peer Comments:

1. This is a good idea, and the prototype looks pretty good. Is it possible to make it smaller? What is the size supposed to be for this

2. I love the idea of a gesture alarm! A few questions: 1) does the gesture alone turn off the alarm or does the person also need to press a button? Just the gesture might be too easy for people who like to oversleep their alarms - for this reason I like the idea of the gesture sensor being on the other side of the room so the person actually has to get up and will be less likely to go back to sleep. 2) It could be safer/cleaner to hide the wires at the top on the inside of the box. 3) It might be helpful to add some words/text to the prototype so people can have a hint of how to interact with the device (on/off/where the sensor is located etc.).

3. You may want to consider the limitations of the proximity sensor in terms of distance. In your diagrams it seemed like the alarm was far away from the user. Also there should be consideration for the size of the screen as well, since the text may not be visible to the user. Is there any way to detect false inputs?


### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:

__Iteration 1:__
* "Looks like": The alarm clock is a rectangle box, and it has the following components on the same side.
One screen to show the current time and indicate the status of gestures.
A servo motor to indicate UDLR(Up, Down, Left,Right) gesture instructions.
A speaker to make sounds as the waking up alarm.
A gesture sensor where users can make gestures close to.

* "Works like": The alarm clock can display the current time, make sounds to wake the user up, and generate random gesture instructions for users to follow. Once the alarm rings, the servo motor will rotate to a certain angle which indicates UDLR, and the user needs to make corresponding gestures near the gesture sensor. If the user makes a correct gesture, the screen will turn to green and automatically show a next gesture, otherwise the screen will turn to red.

* "Acts like": The user interacts with the device by the action of waking up to the alarm sound from the clock and turning it off. Instead of just using one button to turn off the alarm, the user has to perform a set of gestures displayed on the screen. The user gets the instruction for the gesture actions throuh the servo motor. The screen displaying the clock changes the background color to green if the correct gesture is performed, else it turns red. This acts as a feedback for the user if they have performed the correct gesture. There is also feedback in the form of sound where two different sounds are played depending on whether the user is right or wrong.

https://user-images.githubusercontent.com/64258179/138709308-cff5a6ac-8377-4646-aa91-a6104f4a57f6.mp4

__Updates made for Iteration 2:__
1. The screen now displays current time and the remaining number of gestures to be performed.
2. When all the gestures are performed, a mission passe soud is triggered.

__Iteration 2:__
* "Looks like": The alarm clock is a rectangle box, and it has the following components on the same side.
A display screen, one to show the current time and the number of gesture actions to be performed to turn of the alarm.
Using the servo motor to indicate UDLR(Up, Down, Left,Right) gesture instructions.
A speaker makes sounds as the waking up alarm.
A gesture sensor where users can make gestures close to.

* "Works like": The alarm clock can display the current time, make sounds to wake the user up, and generate random gesture instructions for users to follow. Once the alarm rings, the servo motor will rotate to a certain angle which indicates UDLR which will show the icon of directions, and the user needs to make corresponding gestures near the gesture sensor. If the user makes a correct gesture, the gesture screen will turn to green along with a victory sound feedback, otherwise the gesture screen will turn to red. The screen also provides information on how many gestures are suppose to be performed by the user to top the alarm.

* "Acts like":The user interacts with the device by the action of waking up to the alarm sound from the clock and turning it off. Instead of just using one button to turn off the alarm, the user has to perform a set of gestures displayed on the screen. When the user performs a gesture they get feedback for their gesture through the color of the screen that changes to green if the right gesture is performed, else it changes to red. They also get a feedback in terms of the remaining number of gestures to be performed to turn off the alarm. Another modality of feedback is through sound where a ta-da is played when the user performs the correct gesture. When the user finishes all the gestures, the classical Grand Theft Auto (GTA) mission passed sound effect will be triggered. All these actions and feedbacks are aimed at increasing the interaction of the device with the user thereby making it easier for the user to wake up in the morning.

https://user-images.githubusercontent.com/64258179/138713430-d3f2bfc8-44b2-4cb9-98ba-e856a7798310.mp4
