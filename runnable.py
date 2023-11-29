import keyboard
import openai
from openai import whisper

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Define a function to record audio when the spacebar is pressed
def record_audio():
    whisper.start()
    keyboard.wait('space')
    whisper.stop()

# Convert the recorded audio into text
def transcribe_audio():
    audio = whisper.transcribe()
    return audio['text']

# Process the transcribed text using ChatGPT
def process_text(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Main program
def main():
    record_audio()
    transcribed_text = transcribe_audio()
    response = process_text(transcribed_text)
    print(response)

if __name__ == '__main__':
    main()
