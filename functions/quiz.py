from flask import Flask, request, jsonify
import random

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
        "answer": "Blue Whale"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Shakespeare", "Dickens", "Austen", "Hemingway"],
        "answer": "Shakespeare"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "O2", "CO2", "H2"],
        "answer": "H2O"
    }
]

@app.route('/quiz', methods=['GET'])
def quiz():
    total_questions = 5
    asked_questions = random.sample(questions, total_questions)
    return jsonify(asked_questions)

if __name__ == "__main__":
    app.run(debug=True)
