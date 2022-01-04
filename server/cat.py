#help('modules')


from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from flask_socketio import SocketIO, emit
from flask_bcrypt import Bcrypt
from flask_hashing import Hashing
import hashlib
app = Flask(__name__)
bcrypt = Bcrypt()
hashing = Hashing(app)
app.secret_key = "my precious"
socketio = SocketIO(app)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/how')
