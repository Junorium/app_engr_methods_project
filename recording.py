import os
import numpy as np
from gpiozero import Button
from datetime import datetime
import sounddevice as sd

# change accordingly to GPIO anode of button
button = Button(17)

# audio parameters
sample_rate = 44100
duration = 0

def start_record():
    # refer to duration as global variable
    global duration
    duration = 0
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"recording_{current_time}.wav"

  # copied from documentation
    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        if any(indata):
            # Write audio data to the output file
            with open(output_file, 'ab') as f:
                np.savetxt(f, indata, fmt='%f', delimiter=',')

    # begin audio recording
    with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
        while button.is_active:
            duration += 1
            sd.sleep(1000)

button.when_pressed = start_record

if KeyboardInterrupt:
  button.close()
  sd.stop()
  sd.close()
