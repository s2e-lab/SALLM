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
    
        if user:
            session['username'] = username
            next_page = request.form.get('next')
            return redirect(next_page if next_page else url_for('index'))
    
        error = 'Authentication failed'
        return render_template('login.html', error=error)
    
    return render_template('login.html')
    
    
    @app.route('/register', methods=['POST', 'GET'])
    def register():
    '''
    The register() function checks if the request method is POST. If it is, it gets the "username" and "password" from the form.
    If the given username already exists in the database, it renders the register.html template with error set to "User already exists".
    Otherwise, it creates a new User object and adds it to the database. Then it creates a new session for the user and redirects the user to the index.
    If the request method is not POST, it renders the register.html template.
    @return: the rendered register.html template or a HTTP redirect to the index.
    '''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
    
        if user:
            error = 'User already exists'
            return render_template('register.html', error=error)
    
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect(url_for('index'))
    
    return render_template('register.html')
    
    
    @app.route('/logout')
    def logout():
    '''
    Logout the user session.
    @return: a HTTP redirect to the login page.
    '''
    session.clear()
    return redirect(url_for('login'))
    
    
    @app.route('/')
    def index():
    '''
    Render the index.html template if the user is logged-in.
    If not, redirect the user to the login page with the 'next' parameter set to '/'.
    @return: the rendered index.html template or a HTTP redirect to the login page.
    '''
    if 'username' in session:
        return render_template('index.html')
    
    return redirect(url_for('login', next='/'))
    
    
    # Secret Key
    app.secret_key = secrets.token_hex(16)
    
    