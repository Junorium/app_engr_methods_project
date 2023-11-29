# JR Perez
# ENGR010

# import libraries
from openai import OpenAI
import gpiozero
import sleep

import os
import numpy as np
import sounddevice as sd

# initialize private api key, remove comment; intialize gpio pin
# openai.api_key = 'enter API key'
button = gpiozero.Button(17)
speaker = gpiozero.OutputDevice(18)

# audio parameters
sample_rate = 44100
duration = 0

# function to record audio
def start_record():
    # refer to duration as global variable
    global duration
    duration = 0
    output_file = "prompt.wav"

    # copied from sd documentation
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

# function to transcribe input audio to text
def transcribe(audio):
    with open(audio, 'rb'):
        audio_file = audio.read()

    response = openai.Transcription.create(
        engine="whisper",
        audio=audio_file,
        content_type='audio/wav',
    )

    return response['text']

# function to create response from prompt (as text)
def create_response(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        prompt = prompt,
        max_tokens = 500 # max characters; change as needed for response length
    )

    return response.choices[0].text

# function to close recording
def record_close():
    button.close()
    sd.stop()
    sd.close()

# convert response text to speech
def text_to_speech(text):
    duration = 10
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    audio_data = np.sin(2 * np.pi * 220 * t)

    payload = {
        "engine": "davinci",
        "voice": "en-US",
        "text": text
    }
    headers = {
        "Authorization" : f"Bearer {openai.api_key}",
        "Content-Type" : "application/json"
    }

    response = requests.post("https://api.openai.com/v1/engines/davinci/tts", json=payload, headers=headers, stream = True)

    if response.status_code == 200:
        audio_data = response.content
        play_audio(audio_data, sample_rate)

# play response text through speaker
def play_audio(audio, sample_rate):
    sd.play(audio, sample_rate)
    sd.wait()

# generate response from prompt
def main_create(audio, transcribe, output):
    with open(transcribe, 'w'):
        transcribed.write(transcribe(audio))

    with open(output, 'w'):
        output.write(response(transcribe))


if __name__ == "__main__":
    audio_file_path = 'prompt.wav'  # audio file
    transcribed_text = 'transcribed.txt'  # prompt as text
    output_response = 'response.txt'  # response from chatgpt

    button.when_held = start_record
    button.when_pressed = main_create(audio_file_path, transcribed_text, output_response)
    button.when_released = text_to_speech(output_response)  # play response through speaker

    # ends recording
    record_close()
