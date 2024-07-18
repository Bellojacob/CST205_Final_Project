from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# flask --app app --debug run


app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/results')
def results():
    return render_template('results.html')
