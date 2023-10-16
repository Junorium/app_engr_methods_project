# https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/#
'''
# procedure to getting an API
pip install -openai
https://console.cloud.google.com/welcome/new?walkthrough_id=speech-to-text__speech-studio-transcriptions&project=engr010-project
'''

# import libraries
import openai
import gpiozero
import sleep

from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1 import enums

# initialize api keys
openai.api_key = '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'

def transcribe(input_audio):
  client = speech.SpeechClient()
  config = 

  with open(input_audio, 'rb') as audio_file:
    content = audio_file.read()

  response = client.recognize(
    {
    "language_code" : "en-US", 
    "enable_word_time_offsets" : True,
    },
    audio = {"content" : content}
  )

return response

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

if __name__ == "__main__":
  audio_file_path = '.mp3' # audio file
  transcribed_text = '.txt' # intermediate text file
  output_response = '.txt' # response from chatgpt
  
  with open(transcribed_text, 'w'):
    transcribed_text.write(transcribe(audio_file_path))

  with open(output_response, 'w'):
    output_response.write(response(transcribed_text))
