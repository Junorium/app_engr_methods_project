# Rapsberry Pi OpenAI Device
The 3D printed chassis fits a Raspberry Pi 3 B+.  
Printable STL file is attached with .zip file.
Python 3 must be reinstalled prior.

<li>
  <ul>USB Microphone</ul>
  <ul>Tactile Button</ul>
  <ul>Male-to-Female Wires</ul>
</li>

# Wiring
With a tactile button, attach the positive terminal to pin 17 and the negative terminal to GND.
With the speaker, attach the cathode to pin X and the anode to GND.

Connect a continuous 5V power supply to the Rapsberry Pi.

# Installation
## Install in Raspberry Pi terminal prior to running program
```
>>> pip install gpiozero
>>> pip install openai
```
