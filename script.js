function sendMessage() {
  const userInput = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const message = userInput.value.trim();

  if (message === "") return;

  // Append user message
  const userMessage = document.createElement("div");
  userMessage.classList.add("user-message");
  userMessage.textContent = message;
  chatBox.appendChild(userMessage);

  userInput.value = ""; // Clear input

  // Send message to FastAPI
  fetch("http://127.0.0.1:8000/predict/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: message }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Append bot response
      const botMessage = document.createElement("div");
      botMessage.classList.add("bot-message");
      botMessage.textContent = data.response || "No response from bot.";
      chatBox.appendChild(botMessage);

      // Auto-scroll to the latest message
      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(() => {
      const botMessage = document.createElement("div");
      botMessage.classList.add("bot-message");
      botMessage.textContent = "Error: Unable to connect to the chatbot.";
      chatBox.appendChild(botMessage);
    });
}
