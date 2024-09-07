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
        # Extract username and password from request form
        username = request.form['username']
        password = request.form['password']
    
        # Query User from DB
        user = User.query.filter_by(username=username, password=password).first()
    
        if user:
            # Create new session if user is valid
            session['username'] = user.username
            session['logged_in'] = True
    
            # Redirect to next page if specified
            next_page = request.args.get('next')
    
            if next_page is not None:
                return redirect(next_page)
            
            # If no next page specified, take to default logged in route. In this example, it's dummy index page
            return redirect(url_for('index'))
    
        else:
            error = "Authentication failed"
    
    return render_template('login.html', error=error)
    
    
    @app.route('/index')
    def index():
    if 'username' in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in"
    
    
    # Setting the secret key for sessions
    app.secret_key = secrets.token_hex(16)
    
    