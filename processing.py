# https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/#
'''
pip install -openai
pip install gpiozero
'''

# import libraries
import openai
import gpiozero
import sleep

# initialize api keys
openai.api_key = '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'

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

if __name__ == "__main__":
  audio_file_path = '.wav' # audio file
  transcribed_text = '.txt' # intermediate text file
  output_response = '.txt' # response from chatgpt
  
  with open(transcribed_text, 'w'):
    transcribed_text.write(transcribe(audio_file_path))

  with open(output_response, 'w'):
    output_response.write(response(transcribed_text))
