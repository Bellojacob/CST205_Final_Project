from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from quiz_info import quiz_info

# flask --app app --debug run
# Test push- Shane
# Carson's test push just making sure it's all good.

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# homepage 
@app.route('/')
def home():
    return render_template('index.html', quiz_info=quiz_info)

# quiz page
@app.route('/quiz/<quiz_title>')
def quiz(quiz_title):
    # grab the quiz that is chosen from homepage
    selected_quiz = next((quiz for quiz in quiz_info if quiz['quiz_title'] == quiz_title), None)
    return render_template('quiz.html', quiz=selected_quiz)

# results page
@app.route('/results', methods=['POST'])
def results():
    # get the quiz title from the form that is submitted, then check that the quiz is valid
    quiz_title = request.form.get('quiz_title')
    selected_quiz = next((quiz for quiz in quiz_info if quiz['quiz_title'] == quiz_title), None)
    
    if not selected_quiz:
        return redirect(url_for('home'))

    # get total number of questions, and set up variable to hold number of correct answers
    total_questions = len(selected_quiz['questions'])
    correct_answers = 0

    # check each question from out selected quiz, and if our selected answer is true, then add 1 to correct answers variable
    for question in selected_quiz['questions']:
        selected_answer = request.form.get(f'question_{question["id"]}')
        if selected_answer and question['answers'][selected_answer]:
            correct_answers += 1

    return render_template('results.html', total_questions=total_questions, correct_answers=correct_answers)