# Rapsberry Pi OpenAI Device (Main Program)
The 3D printed case fits a Raspberry Pi 3 B+.  
Printable STL file is attached with .zip file.

<h1>Materials</h1>
<li>
  <ul><a href="https://www.amazon.com/KISEER-Microphone-Desktop-Recording-YouTube/dp/B071WH7FC6/ref=sr_1_3?crid=FJIDSW51HA6X&keywords=usb+microphone+raspberry+pi&qid=1701186681&sprefix=usb+microphone+raspberry+pi%2Caps%2C101&sr=8-3">USB Microphone</a></ul>
  <ul><a href="https://www.amazon.com/WOWOONE-12x12x7-3-Tactile-Momentary-Assortment/dp/B08JLWTQ3C/ref=sr_1_2_sspa?crid=1AOOVLP2HAS5P&keywords=tactile+button&qid=1701186342&sprefix=tactile+buton%2Caps%2C71&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1">Tactile Button</a></ul>
  <ul><a href="https://www.amazon.com/EDGELEC-Breadboard-1pin-1pin-Connector-Multicolored/dp/B07GD312VG/ref=sr_1_3?crid=2FLHPMWDB4DLU&keywords=female%2Bto%2Bfemale%2Bjumper&qid=1701310886&sprefix=female%2Bto%2Bfemale%2Bjumper%2Caps%2C69&sr=8-3&th=1">Male-to-Female Jumper Wires</a></ul>
  <ul><a href="https://www.amazon.com/Stainless-Drilling-Lengths-Available-Phillips/dp/B08MQ5CLSD/ref=sr_1_3?crid=NZ255TMOQ7DD&keywords=6x1%2Bself%2Btapping%2Bscrews&qid=1701310966&sprefix=6x1%2Bself%2Btapping%2Bscrews%2Caps%2C60&sr=8-3&th=1">2 Self-Tapping Screws (#6 x 1")</a></ul>
  <ul>Device Case (provided)</ul>
</li>

<h1>Wiring</h1>
With a tactile button, attach the positive terminal to pin 17 and the negative terminal to GND.
Attach the tactile button unto the front left panel of the device case, where the two slots of pins can slip through the slits.
With the speaker, attach the cathode to pin 18 and the anode to GND.
Use the self-tapping screws to attach the speaker in place once connected.

Connect a continuous 5V power supply to the Rapsberry Pi.

<h1>API Keys</h1>
Prior to running the program, you must create a free [OpenAI account](https://openai.com/blog/openai-api).
Create a private API key and substitute in line 14 of main.py, removing the comment at the start to initialize the API key.

<h1>Testing</h1>
In order to test the device, once running, use the following templates:

> Create a set of 20 flash cards along the AP Chemistry curriculum about Kinetics.

> Create a problem set of 30 questions regarding Related Rates along college-level Calculus curricula.

> Give me an example of the use of recusion in coding across different coding languages.

> Create a list of prompts I could use to brainstorm topics for my introductory philosophy course.

# Alternative Program
Run this program instead if materials for main program is unfeasible.

<h1>Materials</h1>
<li>
  <ul>MacOS Environment</ul>
  <ul>Prerecorded .mp3 File</ul>
</li>

<h1>API Keys</h1>
Prior to running the program, follow the previous instructions an create a private API key in line 4 of alternative.py, removing the comment at the start to initialize the API key.

<h1>Testing</h1>
Remember to record a prompt and save it as a .mp3 file in the same directory as the alternate program.
Save the file as "audio.mp3" or change line 7.

Use similar prompts as above.
