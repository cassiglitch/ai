function sendMessage() {
  // Get user input
  const userInput = document.getElementById("user_input").value;
  
  // Create user message element
  const userMessageElement = document.createElement("li");
  userMessageElement.classList.add("user");
  userMessageElement.textContent = userInput;
  
  // Add user message to conversation
  const conversationElement = document.getElementById("conversation");
  conversationElement.appendChild(userMessageElement);
  
  // Send user input to server for processing
  fetch("/api/chatbot", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ "input": userInput })
  })
  .then(response => response.json())
  .then(data => {
    // Create bot message element
    const botMessageElement = document.createElement("li");
    botMessageElement.classList.add("bot");
    botMessageElement.textContent = data.output;
    
    // Add bot message to conversation
    conversationElement.appendChild(botMessageElement);
    
    // Scroll to bottom of conversation
    conversationElement.scrollTop = conversationElement.scrollHeight;
  });
}
