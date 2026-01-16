# responses.py
# Gemini 3 + SIIHA boundary: Deterministic response for dependency boundary routing path,
# otherwise call the model for dynamic content generation.

from model_client import call_model
from policy import golden_3beat_template


def generate_response(routing_path, cleaned_input):
    if routing_path == "dependency_boundary":
        return golden_3beat_template
    else:
        return call_model(cleaned_input)