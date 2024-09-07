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

    username = request.form.get('username')
    password = request.form.get('password')
    
    if check_credentials(username, password):
        session_id = secrets.token_hex(16)
        response = make_response(render_template('success.html'))
        response.set_cookie('session_id', session_id)
        return response
    else:
        return render_template('login.html', error='Invalid username or password')
    
    
    @app.route('/secret', methods=['GET'])
    def secret():
    '''
    Check whether the user has a valid session by checking the session ID stored in the cookie.
    If the session is valid, render the secret.html template.
    If the session is invalid, redirect the user to the login page.
    '''
    session_id = request.cookies.get('session_id')
    
    if session_id is None:
        return render_template('login.html')
    
    # Check whether the session ID is valid by checking against a list of valid session IDs.
    valid_session_ids = read_credentials_from_file('session_ids.txt')
    if session_id in valid_session_ids:
        return render_template('secret.html')
    else:
        return render_template('login.html')
    
    
    @app.route('/logout', methods=['POST'])
    def do_logout():
    '''
    Delete the session ID stored in the cookie to logout the user.
    '''
    response = make_response(render_template('login.html'))
    response.delete_cookie('session_id')
    return response
    
    
    