# Rapsberry Pi OpenAI Device
The 3D printed chassis fits a Raspberry Pi 3 B+.  
Printable STL file is attached with .zip file.

<li>
  <ul>[USB Microphone](https://www.amazon.com/KISEER-Microphone-Desktop-Recording-YouTube/dp/B071WH7FC6/ref=sr_1_3?crid=FJIDSW51HA6X&keywords=usb+microphone+raspberry+pi&qid=1701186681&sprefix=usb+microphone+raspberry+pi%2Caps%2C101&sr=8-3)</ul>
  <ul>[Tactile Button](https://www.amazon.com/WOWOONE-12x12x7-3-Tactile-Momentary-Assortment/dp/B08JLWTQ3C/ref=sr_1_2_sspa?crid=1AOOVLP2HAS5P&keywords=tactile+button&qid=1701186342&sprefix=tactile+buton%2Caps%2C71&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)</ul>
  <ul>Male-to-Female Jumper Wires</ul>
  <ul>2 Self-Tapping Screws</ul>
  <ul>Device Chassis (provided)</ul>
</li>

# Wiring
With a tactile button, attach the positive terminal to pin 17 and the negative terminal to GND.
With the speaker, attach the cathode to pin X and the anode to GND.

Connect a continuous 5V power supply to the Rapsberry Pi.

# Installation
[Python 3](https://www.python.org/downloads/) must be installed prior to installing the following libraries.
Install the following in Raspberry Pi terminal prior to running program
```
>>> pip install gpiozero
>>> pip install openai
>>> pip install sounddevice
```

# API Keys
Prior to running the program, you must create a free [OpenAI account](https://openai.com/blog/openai-api).
Create a private API key and substitute in line X of main.py, removing the comment at the start to initialize the API key.

# Testing
In order to test the device, once running, use the following templates:
