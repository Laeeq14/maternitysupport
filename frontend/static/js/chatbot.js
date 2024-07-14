// chatbot.js

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('chat-form');
    const inputField = document.getElementById('user-input');
    const chatbotContainer = document.getElementById('chatbot-container');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const userInput = inputField.value.trim();
        inputField.value = '';

        if (userInput === '') {
            return;
        }

        // Append user message to chatbot container
        appendMessage(`You: ${userInput}`, 'user');

        // Send user message to server (replace with actual endpoint)
        const response = await fetch('/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        });

        if (!response.ok) {
            console.error('Failed to send message to server.');
            return;
        }

        const responseData = await response.json();
        const botResponse = responseData.response;

        // Append bot response to chatbot container
        appendMessage(`Bot: ${botResponse}`, 'bot');
    });

    function appendMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', sender);
        messageElement.textContent = message;
        chatbotContainer.appendChild(messageElement);
        
        // Scroll to bottom of chat on new message
        chatbotContainer.scrollTop = chatbotContainer.scrollHeight;
    }

    // Toggle chatbot visibility
    const chatbotLink = document.getElementById('chatbot-link');
    const chatbotSection = document.getElementById('chatbot');

    chatbotLink.addEventListener('click', (e) => {
        e.preventDefault();
        chatbotSection.style.display = chatbotSection.style.display === 'none' ? 'block' : 'none';
    });
});
