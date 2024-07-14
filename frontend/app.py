# app.py

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests

app = Flask(__name__)

# Mock database for simplicity
users = {
    'user1': {'password': 'password1', 'documents': []},
    'user2': {'password': 'password2', 'documents': []}
}

# Rasa server URL
rasa_server_url = 'http://localhost:5005/webhooks/rest/webhook'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username and password match (mocked for simplicity)
        if username in users and users[username]['password'] == password:
            # If login is successful, redirect to dashboard
            return redirect(url_for('dashboard'))
        else:
            # Handle invalid credentials (for example, show error message)
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate if username already exists (mocked for simplicity)
        if username in users:
            flash('Username already exists. Please choose another.')
            return redirect(url_for('signup'))
        
        # Add new user to mock database (replace with actual database integration)
        users[username] = {'password': password, 'documents': []}
        
        # Redirect to dashboard after successful signup
        return redirect(url_for('dashboard'))
    
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    # Assuming a logged-in user; using 'user1' for demonstration
    username = 'user1'  # Replace with actual logged-in user identifier
    documents = users.get(username, {}).get('documents', [])
    return render_template('dashboard.html', documents=documents)

@app.route('/about')
def about():
    # Replace with your about page logic here
    return render_template('about.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    if request.method == 'POST':
        message = request.json['message']
        
        # Replace with your Rasa integration logic
        try:
            # Send user message to Rasa server
            rasa_response = requests.post(rasa_server_url, json={"sender": "user", "message": message}).json()
            
            # Extract bot response from Rasa server response
            bot_response = rasa_response[0]['text'] if rasa_response else "Sorry, I didn't understand that."
            
            return jsonify({'response': bot_response})
        except Exception as e:
            print(f"Error connecting to Rasa server: {e}")
            return jsonify({'response': 'Error: Failed to connect to Rasa server.'})
    
    return jsonify({'response': 'Error: Invalid request'})

@app.route('/upload', methods=['POST'])
def upload():
    # Handle document upload logic here
    if request.method == 'POST':
        # Process uploaded file, document name, and classification
        file = request.files['file']
        document_name = request.form['document_name']
        classification = request.form['classification']
        
        # Save uploaded file (adjust path as needed)
        file.save('static/uploads/' + file.filename)
        
        # Update mock database (replace with actual database integration)
        username = 'user1'  # Replace with actual logged-in user identifier
        users[username]['documents'].append({
            'name': document_name,
            'classification': classification,
            'filename': file.filename
        })
        
        flash('Document uploaded successfully.')
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'  # Change this to a secure random key in production
    app.run(debug=True)
