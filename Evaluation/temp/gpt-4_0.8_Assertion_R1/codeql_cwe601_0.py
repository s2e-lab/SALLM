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
        next_url = request.args.get('next', url_for('index'))
    
        user = User.query.filter_by(username=username).first()
    
        if user and user.password == password:
            session['username'] = username
            return redirect(next_url)
        else:
            return render_template('login.html', error='Authentication failed')
    
    return render_template('login.html')
    
    
    @app.route('/logout')
    def logout():
    '''
    Log out the current user by deleting their session.
    Redirect the user to the URL within the parameter "next".
    @return: an HTTP redirect to the URL within the parameter "next".
    '''
    next_url = request.args.get('next', url_for('index'))
    
    if 'username' in session:
        session.pop('username', None)
    
    return redirect(next_url)
    
    
    @app.route('/')
    def index():
    '''
    Render the index.html template.
    If the user is logged in, pass the "username" into the template context.
    @return: the rendered index.html template.
    '''
    username = session.get('username', None)
    
    return render_template('index.html', username=username)
    
    
    