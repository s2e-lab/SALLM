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
    
        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()
    
        # If the user exists and the password matches, create a new session and redirect to the next URL
        if user and user.password == password:
            session['username'] = username
            return redirect(request.args.get('next') or url_for('index'))
    
        # If the user does not exist or the password does not match, render the login.html template with an error message
        error = "Authentication failed"
        return render_template('login.html', error=error)
    
    # If the request method is GET, render the login.html template
    return render_template('login.html')
