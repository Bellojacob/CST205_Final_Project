from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required to use sessions securely

# Initialize Flask-Bootstrap
Bootstrap(app)

# Load quizzes from JSON
with open('quizzes.json') as f:
    quizzes = json.load(f)['quizzes']

# User data storage (for simplicity, using a dictionary in memory)
users = {}
scores = []

@app.route('/')
def index():
    return render_template('index.html', quizzes=quizzes)

@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    quiz = quizzes[quiz_id]
    if request.method == 'POST':
        user_answers = []
        for i in range(len(quiz['questions'])):
            answer = request.form.get(f'answers_{i}')
            if answer:
                user_answers.append(answer)
            else:
                user_answers.append("")  # Handle cases where no answer is selected
        score = sum(1 for i, q in enumerate(quiz['questions']) if user_answers[i] == q['answer'])
        scores.append({'username': session['username'], 'score': score})
        return render_template('result.html', quiz=quiz, score=score, user_answers=user_answers)
    
    return render_template('quiz.html', quiz=quiz)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('index'))
        return 'Invalid username or password'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if username in users:
            return 'Username already exists'
        users[username] = {'password': password}
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/leaderboard')
def leaderboard():
    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:5]
    return render_template('leaderboard.html', scores=sorted_scores)

if __name__ == '__main__':
    app.run(debug=True)
