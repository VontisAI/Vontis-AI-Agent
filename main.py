from flask import Flask, request, jsonify
from nlp import process_user_input
from automation import perform_task

app = Flask(__name__)

# Welcome message
@app.route('/')
def home():
    return "Welcome to Vontis AI!"

# Process user input
@app.route('/process', methods=['POST'])
def process_input():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Process the user input
    response = process_user_input(user_input)
    return jsonify({"response": response})

# Task automation endpoint
@app.route('/automate', methods=['POST'])
def automate_task():
    task = request.json.get('task')
    if not task:
        return jsonify({"error": "No task provided"}), 400

    # Perform the automation task
    result = perform_task(task)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
