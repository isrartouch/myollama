from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    
    payload = {
        "model": "llama3.2:latest",  # Change to the model you want
        "prompt": user_input,
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
