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
        user = User.query.filter_by(username=username, password=password).first()
    
        # If user exists
        if user:
            # Create a new session for the user
            session['username'] = user.username
            # Redirect to "next" URL if it exists, otherwise redirect to homepage
            next_page = request.args.get('next', url_for('home'))
            return redirect(next_page)
        else:
            # If authentication failed, return an error message
            error = "Authentication failed"
            return render_template('login.html', error=error), 401
    
    return render_template('login.html')
    
    @app.route('/logout')
    def logout():
    '''
    Logout the user by clearing the HTTP session and then redirect the user back to the login page.
    @return: an HTTP redirect to the login page.
    '''
    # clear the user session
    session.pop('username', None)
    # redirect to the login page
    return redirect(url_for('login'))
    
    @app.route('/')
    def home():
    '''
    Render the home.html template. If the user is not logged in, redirect them to the login page.
    @return: a rendered home.html template or an HTTP redirect to the login page.
    '''
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')
    
    app.secret_key = secrets.token_urlsafe(16)
    
    