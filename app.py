from flask import Flask, request, jsonify
from utils import detect_emotion, format_output

app = Flask(__name__)

@app.route('/emotion', methods=['POST'])
def emotion():
    try:
        text = request.json.get('text')
        emotions = detect_emotion(text)
        return jsonify(format_output(emotions))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
