import torch
import transformers
from flask import Flask, request, jsonify

# Load the DialoGPT model and tokenizer
tokenizer = transformers.DialoGPTTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = transformers.DialoGPT2LMHeadModel.from_pretrained("microsoft/DialoGPT-medium")

# Define a function to generate responses using the DialoGPT model
def generate_response(user_input):
    # Encode user input
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    
    # Generate response from model
    response_ids = model.generate(
        input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.9,
        top_k=50,
        temperature=0.8
    )
    
    # Decode response
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    
    return response

app = Flask(__name__)

# Define an API endpoint for the chatbot
@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    # Get user input from request
    user_input = request.json["input"]
    
    # Generate response from chatbot using the DialoGPT model
    response = generate_response(user_input)
    
    # Return response as JSON
    return jsonify({ "output": response })

# Run the Flask app
if __name__ == "__main__":
    app.run()
