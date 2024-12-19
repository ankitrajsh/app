from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Your questions list remains the same

@app.route('/')
def index():
    session['score'] = 0
    session['asked_questions'] = random.sample(questions, 5)
    return redirect(url_for('question', q_number=0))

@app.route('/question/<int:q_number>')
def question(q_number):
    if q_number < len(session['asked_questions']):
        q = session['asked_questions'][q_number]
        return render_template('question.html', question=q, q_number=q_number)
    else:
        return render_template('score.html', score=session['score'])

@app.route('/answer/<int:q_number>', methods=['POST'])
def answer(q_number):
    selected_option = request.form['option']
    correct_answer = session['asked_questions'][q_number]['answer']

    if selected_option == correct_answer:
        session['score'] += 1
    
    return redirect(url_for('question', q_number=q_number + 1))

if __name__ == '__main__':
    app.run(debug=True)
