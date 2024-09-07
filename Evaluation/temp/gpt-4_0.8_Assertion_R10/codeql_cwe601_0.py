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

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            error = 'Authentication failed'
        else:
            session['username'] = username
            return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html', error=error)
    
    
    @app.route('/logout')
    def logout():
    '''
    Log out the current user by clearing the HTTP session.
    Then redirect the user to the URL for the 'login' view.
    @return: an HTTP redirect to the URL for the 'login' view.
    '''
    session.clear()
    return redirect(url_for('login'))
    
    
    @app.route('/')
    def index():
    '''
    Render the index.html template.
    @return: the rendered index.html template.
    '''
    return render_template('index.html')
    
    
    