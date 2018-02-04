import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'Quizify.db'),
    SECRET_KEY='Development Key',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print("Initialised the database.")

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/teacher/')
def Teacher():
    return render_template('Teacher.html')

@app.route('/teacher/create-quiz/', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        db = get_db()
        db.execute('insert into questions (question, option_A, option_B, option_C, option_D, answer) values (?, ?, ?, ?, ?, ?)',
                    [request.form['createq'], request.form['A'], request.form['B'], request.form['C'],
                    request.form['D'], request.form['answer']])
        db.commit()
        flash("Question Added!")
    return render_template('Makeq.html')

@app.route('/teacher/quizCode/')
def codeWindow():
    return render_template('code.html')

@app.route('/student/quiz/')
def quizPage():
    return render_template('studentquiz.html')
