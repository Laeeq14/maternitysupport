document.addEventListener('DOMContentLoaded', () => {
    const healthInfoLink = document.getElementById('health-info-link');
    const chatbotLink = document.getElementById('chatbot-link');
    const healthInfoSection = document.getElementById('health-info');
    const chatbotSection = document.getElementById('chatbot');

    healthInfoLink.addEventListener('click', (e) => {
        e.preventDefault();
        healthInfoSection.style.display = 'block';
        chatbotSection.style.display = 'none';
    });

    chatbotLink.addEventListener('click', (e) => {
        e.preventDefault();
        healthInfoSection.style.display = 'none';
        chatbotSection.style.display = 'block';
    });
});
