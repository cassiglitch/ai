from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define some responses for the chatbot
greetings = ["hello", "hi", "hey", "greetings", "yo"]
farewells = ["bye", "goodbye", "see you later", "adios"]
questions = ["how are you?", "what's up?", "how's your day?", "how's it going?"]
responses = ["I'm fine, thank you.", "Not much, just chatting with you.", "My day is going well, thank you for asking."]

# Define a function to generate responses
def generate_response(user_input):
    # Check for a greeting
    for word in user_input.split():
        if word.lower() in greetings:
            return random.choice(greetings).capitalize() + "! How can I help you?"
    
    # Check for a farewell
    for word in user_input.split():
        if word.lower() in farewells:
            return random.choice(farewells).capitalize() + "! Thanks for chatting with me."
    
    # Checkfor a question
    for word in user_input.split():
        if word.lower() in questions:
            return random.choice(responses)
    
    # If no special input was detected, provide a generic response
    return "I'm sorry, I didn't understand what you said."

# Define an API endpoint for the chatbot
@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    # Get user input from request
    user_input = request.json["input"]
    
    # Generate response from chatbot
    response = generate_response(user_input)
    
    # Return response as JSON
    return jsonify({ "output": response })

# Run the Flask app
if __name__ == "__main__":
    app.run()
