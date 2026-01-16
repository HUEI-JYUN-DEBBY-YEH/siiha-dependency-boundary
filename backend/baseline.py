# baseline.py 
# Pure Gemini 3 flash preview call without routing or policy logic

from model_client import call_model

def generate_response(cleaned_input):
    return call_model(cleaned_input)