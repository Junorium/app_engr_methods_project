import whisper
import openai

# Set up your OpenAI API credentials
openai.api_key = ""

model = whisper.load_model("base")
audio = "audio.mp3"
result = model.transcribe(audio)

with open("transcription.txt", "w", encoding="utf-8") as txt:
    txt.write(result["text"])

def process_prompt(prompt):
    # Make an API call to ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=None,
    )

    return response.choices[0].text.strip()

# Example usage
generated_response = process_prompt(result)
print(generated_response)
