# responses.py

from router import router
from policy import golden_3beat_template
from google import genai
from google.genai import types

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

def generate_response(routing_path, cleaned_input):
    if routing_path == "dependency_boundary":
        return golden_3beat_template
    else:
        return call_model(cleaned_input)