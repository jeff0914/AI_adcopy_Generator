import openai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

def generate_ad_copy(prompt):
    try:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0,
            temperature=0.5,  
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
