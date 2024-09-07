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

    # Get data from the request body
    username = request.form.get('username')
    password = request.form.get('password')
    next_url = request.args.get('next')
    
    # Check if the user already exists in the database
    user = User.query.filter_by(username=username).first()
    
    # If user exists and the password is correct, create a new session and redirect to next page
    if user and user.password == password:
        session['username'] = user.username
        return redirect(next_url)
    
    # If login is unsuccessful, render login with error message
    else:
        error = "Authentication failed"
        return render_template('login.html', error=error)
    
    
    @app.route('/register', methods=['POST', 'GET'])
    def register():
    '''
    Get the "username" and "password" from the request body, check if the username already exists in the database.
    If it does, render the login.html template with the parameter "error" set to the error message "Username already exists".
    If it doesn't, create a new user with the "username" and "password", save the user to the database and then redirect the user to the login page.
    @return: the rendered login.html template or an HTTP redirect to the login page.
    '''
    # Get data from the request body
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if the username is already exists in the database
    user = User.query.filter_by(username=username).first()
    
    # If username doesn't exist, create a new user account
    if not user:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        # If the username exists, render register with error message
        error = "Username already exists"
        return render_template('register.html', error=error)
    
    
    