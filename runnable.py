import whisper
import openai

# Set up your OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define the function to process the text prompt through ChatGPT
def process_text_prompt(prompt):
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

    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()

    return generated_text

# Example usage
prompt = "What is the meaning of life?"
generated_response = process_text_prompt(prompt)
print(generated_response)
