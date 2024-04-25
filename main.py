# JR Perez
# ENGR010

# import libraries
import sys
import os
import numpy as np
import sounddevice as sd
import requests
from gpiozero import Button, OutputDevice

# initialize private api key, remove comment; intialize gpio pin
# openai.api_key = 'enter API key'
button = Button(17)
speaker = OutputDevice(18)

# audio parameters
sample_rate = 44100

# function to record audio
def start_record():
    global duration
    duration = 0
    output_file = "prompt.wav"

    # callback function for recording
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
    with open(audio, 'rb') as f:
        audio_file = f.read()

    response = openai.Transcription.create(
        engine="whisper",
        audio=audio_file,
        content_type='audio/wav',
    )

    return response['text']

# function to create response from prompt (as text)
def create_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=500  # max characters; change as needed for response length
    )

    return response.choices[0].text

# function to close recording
def record_close():
    button.close()
    sd.stop()
    sd.close()

# convert response text to speech
def text_to_speech(text):
    payload = {
        "engine": "davinci",
        "voice": "en-US",
        "text": text
    }
    headers = {
        "Authorization": f"Bearer {openai.api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.openai.com/v1/engines/davinci/tts", json=payload, headers=headers, stream=True)

    if response.status_code == 200:
        audio_data = response.content
        play_audio(audio_data)

# play response text through speaker
def play_audio(audio):
    sd.play(audio, sample_rate)
    sd.wait()

# function to handle main logic
def main():
    audio_file_path = 'prompt.wav'  # audio file
    transcribed_text = 'transcribed.txt'  # prompt as text
    output_response = 'response.txt'  # response from chatgpt

    # Start recording when button is held down
    button.when_held = start_record

    # Process recording and generate response when button is pressed
    button.when_pressed = lambda: main_create(audio_file_path, transcribed_text, output_response)

    # Play response through speaker when button is released
    button.when_released = lambda: text_to_speech(output_response)

    # Close recording
    record_close()

# function to transcribe and generate response
def main_create(audio, transcribed, output):
    transcribed_text = transcribe(audio)
    with open(transcribed, 'w') as f:
        f.write(transcribed_text)

    response_text = create_response(transcribed_text)
    with open(output, 'w') as f:
        f.write(response_text)

# Run the main function
if __name__ == "__main__":
    main()
