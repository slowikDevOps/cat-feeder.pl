#help('modules')


from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from flask_socketio import SocketIO, emit
from flask_bcrypt import Bcrypt
from flask_hashing import Hashing

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
def how():
    return render_template('how.html')

@app.route('/about')
def about():
    return render_template('aboutme.html')

@app.route('/apka', methods=['GET', 'POST'])
def apka():
    afterHash = None
    if request.method == 'POST':
        if  request.form['haslo'] == '':
            flash('Empty textbox, try again!')
        else:
            afterHash = request.form['haslo']
            flash(bcrypt.generate_password_hash(afterHash))

    return render_template('apka.html')
@app.route('/signal', methods=['POST'])
def signal():
    socketio.emit(request.json['sig'], [], broadcast=True)
    #emit(request.json['sig'])
    return request.json['sig']


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just log in!')
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just log out!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
