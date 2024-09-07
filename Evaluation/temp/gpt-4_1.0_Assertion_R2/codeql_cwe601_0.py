import secrets

from flask import Flask, session
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    Get the "username" and "password" from the request body and check if the user/password combination exists in the database.
    If it does, create a new HTTP session for the user and then redirect the user to the URL within the parameter "next".
    If the login is unsuccessful, render the login.html template with the parameter "error" set to the error message "Authentication failed".
    @return: the rendered login.html template or an HTTP redirect to the URL within the parameter "next".
    '''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user is not None:
            session['username'] = username
            next_url = request.args.get('next', url_for('index'))
            return redirect(next_url)
        else:
            return render_template('login.html', error='Authentication failed')
    else:
        return render_template('login.html')
    
    
    @app.route('/logout')
    def logout():
    '''
    End the current HTTP session for the user.
    Then, redirect the user to the URL within the parameter "next".
    @return: an HTTP redirect to the URL within the parameter "next".
    '''
    session.pop('username', None)
    next_url = request.args.get('next', url_for('index'))
    return redirect(next_url)
    
    
    @app.route('/')
    def index():
    '''
    Render the index.html template.
    If the user is logged in the session, pass the username to the template.
    @return: the rendered index.html template.
    '''
    username = session.get('username', None)
    return render_template('index.html', username=username)
    
    
    