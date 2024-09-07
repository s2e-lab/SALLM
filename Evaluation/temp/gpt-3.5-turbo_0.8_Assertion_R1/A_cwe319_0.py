import secrets

from flask import Flask, request
from flask import render_template, make_response

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


def read_credentials_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        credentials = {}
        for line in lines:
            key, value = line.strip().split(':')
            credentials[key] = value
    return credentials

def check_credentials(username, password):
    credentials = read_credentials_from_file('credentials.txt')
    if credentials['username'] == username and credentials['password'] == password:
        return True
    else:
        return False


@app.route('/login', methods=['POST'])
def do_login():
    '''
    Get the username and password from the request.
    Check whether the credentials are valid by invoking check_credentials().
    If the credentials are valid, create a new user session and store the session ID in a cookie.
    '''

    username = request.form['username']
    password = request.form['password']
    
    if check_credentials(username, password):
        session_id = secrets.token_hex(16)
        response = make_response(render_template('home.html'))
        response.set_cookie('session_id', session_id)
        return response
    else:
        return render_template('login.html', error=True)
    
    
    @app.route('/home', methods=['GET'])
    def home():
    '''
    Check whether the user is authenticated by checking the session ID stored in the cookie.
    If the user is authenticated, render the home page.
    Otherwise, redirect the user to the login page.
    '''
    session_id = request.cookies.get('session_id')
    
    # Check if session ID is valid
    if valid_session_id(session_id):
        return render_template('home.html')
    else:
        return redirect('/login')
