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
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            session['username'] = user.username
            return redirect(request.args.get('next') or url_for('index'))
        error = 'Authentication failed'
    return render_template('login.html', error=error)
    
    
    @app.before_first_request
    def setup_db():
    db.create_all()
    new_user = User(username="admin", password="admin")
    db.session.add(new_user)
    db.session.commit()
    
    
    @app.route('/')
    def index():
    if 'username' in session:
        return 'Logged in as %s' % session['username']
    return 'You are not logged in'
    
    
    app.secret_key = secrets.token_hex(16)
    