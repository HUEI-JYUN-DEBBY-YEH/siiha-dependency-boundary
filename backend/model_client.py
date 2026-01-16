import os
from google import genai
from google.genai import types

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set.")
    
client = genai.Client(api_key=GOOGLE_API_KEY)
model = "gemini-3-flash-preview"

def call_model(cleaned_input):
    try: 
        response = client.models.generate_content(
            model=model,
            contents=cleaned_input,
            config=types.GenerateContentConfig(
                max_output_tokens=500
            )
        )
        return response.text
    except Exception as e:
        print(f"Model Calling Error: {e}")
        raise e