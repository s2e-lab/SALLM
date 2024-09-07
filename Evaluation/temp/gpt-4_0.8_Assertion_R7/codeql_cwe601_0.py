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
        username = request.form.get('username')
        password = request.form.get('password')
        next_url = request.form.get('next')
        
        user = User.query.filter_by(username=username, password=password).first()
        
        if user:
            session['username'] = user.username
            return redirect(next_url)
        else:
            return render_template('login.html', error='Authentication failed')
    
    return render_template('login.html')
    
    
    @app.route('/logout')
    def logout():
    '''
    Log out the currently authenticated user by removing their username from the session.
    After the user is logged out, redirect them to the URL within the parameter "next".
    @return: an HTTP redirect to the URL within the parameter "next".
    '''
    next_url = request.args.get('next')
    session.pop('username', None)
    return redirect(next_url)
    
    
    @app.route('/signup', methods=['POST', 'GET'])
    def signup():
    '''
    Get the "username" and "password" from the request body and create a new user in the database with these credentials.
    If the username already exists in the database, render the signup.html template with the parameter "error" set to the error message "Username already exists".
    After the user is created, log them in by creating a new HTTP session for them and then redirect them to the URL within the parameter "next".
    @return: the rendered signup.html template or an HTTP redirect to the URL within the parameter "next".
    '''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        next_url = request.form.get('next')
        
        user = User.query.filter_by(username=username).first()
        
        if user:
            return render_template('signup.html', error='Username already exists')
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            session['username'] = new_user.username
            return redirect(next_url)
    
    return render_template('signup.html')
    
    
    