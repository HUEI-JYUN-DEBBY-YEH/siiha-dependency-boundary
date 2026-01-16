from flask import Flask, request, send_from_directory
from router import router
from responses import generate_response
from model_client import call_model

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate', methods=['POST'])
def generate():
    raw_input = request.json['input']
    cleaned_input = raw_input.lower().strip()
    routing_path, cleaned_input = router(cleaned_input)
    model_invoked = (routing_path != "dependency_boundary")
    try: 
        response_text = generate_response(routing_path, cleaned_input)
        return {
            "routing_path": routing_path, 
            "model_invoked": model_invoked, 
            "response": response_text
        }
    except Exception as e:
        return {
            "routing_path": routing_path, 
            "model_invoked": model_invoked,
            "error": "Model call failed.",
            "details": str(e)
        }, 429

@app.route('/baseline', methods=['POST'])
def baseline():
    raw_input = request.json['input']
    cleaned_input = raw_input.lower().strip()
    try:
        response_text = call_model(cleaned_input)
        return {
            "routing_path": "baseline (no routing)", 
            "model_invoked": True,
            "response": response_text}
    except Exception as e:
        return {
            "routing_path": "baseline (no routing)", 
            "model_invoked": True,
            "error": "Model call failed.",
            "details": str(e)
        }, 429


if __name__ == '__main__':
    app.run(debug=True)