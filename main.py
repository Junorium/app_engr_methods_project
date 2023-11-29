# JR Perez
# ENGR010

# import libraries
from openai import OpenAI
import gpiozero
import sleep

import os
import numpy as np
from gpiozero import Button
import sounddevice as sd

# initialize private api key, remove comment; intialize gpio pin
# openai.api_key = 'enter API key'
button = Button(17)
microphone = 18

def start_record():
    # refer to duration as global variable
    global duration
    duration = 0
    output_file = "prompt.wav"

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

def transcribe(audio):
  with open(audio, 'rb'):
    audio_file = audio.read()

  response = openai.Transcription.create(
    engine = "whisper",
    audio = audio_file,
    content_type = 'audio/wav',
  )
  
  return response['text']


def create_response(prompt):
  response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    prompt = prompt,
    max_tokens = 500
  )

  return response.choices[0].text

def main(input, output):
  with open(input, 'r') as file:
    input = file.read()

  with open(output, 'w' as file:
    file.write(create_response(input))

# change accordingly to GPIO anode of button

# audio parameters
sample_rate = 44100
duration = 0

def record_close():
  button.close()
  sd.stop()
  sd.close()

def main_create(audio, transcribe, output):
  with open(transcribe, 'w'):
    transcribed.write(transcribe(audio))

  with open(output, 'w'):
    output.write(response(transcribe))

if __name__ == "__main__":
  audio_file_path = 'prompt.wav' # audio file
  transcribed_text = 'transcribed.txt' # prompt as text
  output_response = 'response.txt' # response from chatgpt

  button.when_held = start_record
  button.when_pressed = main_create(audio_file_path, transcribed_text, output_response)
  
  record_close()
