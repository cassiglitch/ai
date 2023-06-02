import requests
from flask import Flask, request, jsonify
import time

AI_DUNGEON_API_URL = "https://api.aidungeon.io/generate"

# Define a function to generate responses using the AI Dungeon API
def generate_response(user_input):
    try_count = 0
    while try_count < 3:
        try:
            payload = {
                "story": [f"User: {user_input}\nAI:"],
                "temperature": 0.7,
                "max_tokens": 64,
                "prompt": "",
                "frequency_penalty": 0,
                "presence_penalty": 0
            }

            response = requests.post(AI_DUNGEON_API_URL, json=payload)
            response.raise_for_status()
            result = response.json()["data"][0]["text"].strip()
            
            return result
        except requests.exceptions.RequestException:
            try_count += 1
            time.sleep(1)
    
    raise Exception("Failed to generate response")

app = Flask(__name__)

# Define an API endpoint for the chatbot
@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    # Get user input from request
    user_input = request.json["input"]
    
    # Generate response from chatbot using the AI Dungeon API
    try:
        response = generate_response(user_input)
    except Exception as e:
        response = str(e)
    
    # Return response as JSON
    return jsonify({ "output": response })

# Run the Flask app
if __name__ == "__main__":
    app.run()
