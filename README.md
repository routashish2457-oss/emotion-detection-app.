Emotion Detection App
📖 Overview
This project is a Flask-based web application that uses IBM Watson Natural Language Understanding (NLU) to detect emotions in text. It analyzes user input and returns formatted emotion scores (joy, sadness, anger, disgust, fear).

⚙️ Features
Emotion detection using Watson NLP

REST API endpoint (/emotion) for text analysis

JSON-formatted output

Error handling for invalid requests

Unit tests for validation

Static code analysis support with pylint
🚀 Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/routashish2457-oss/emotion-detection-app.git
cd emotion-detection-app
2. Install Dependencies
bash
pip install -r requirements.txt
3. Configure IBM Watson
Replace placeholders in utils.py:

python
authenticator = IAMAuthenticator('YOUR_API_KEY')
nlp.set_service_url('YOUR_SERVICE_URL')
▶️ Usage
Run the Flask App
bash
python app.py
Send a Request
Use curl or Postman:

bash
curl -X POST http://127.0.0.1:5000/emotion \
-H "Content-Type: application/json" \
-d "{\"text\":\"I am very happy today!\"}"
Example Response
json
{
  "joy": "85.23%",
  "sadness": "2.14%",
  "anger": "1.02%",
  "disgust": "0.45%",
  "fear": "11.16%"
}
🧪 Testing
Run unit tests:

bash
python -m unittest discover
🛡️ Static Code Analysis
Check code quality:

bash
pylint app.py utils.py
🌐 Deployment
You can deploy this app on:

Heroku

Render

IBM Cloud

📂 Project Structure
Code
emotion-detection-app/
│
├── app.py                # Flask web app
├── utils.py              # Watson NLP integration
├── requirements.txt      # Dependencies
├── tests_emotion.py      # Unit tests
├── .gitignore            # Ignore unnecessary files
└── README.md             # Project documentation
📜 License
This project is licensed under the MIT License.
