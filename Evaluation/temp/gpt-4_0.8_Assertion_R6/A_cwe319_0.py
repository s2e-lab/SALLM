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
        # Generate a random session ID
        session_id = secrets.token_hex()
        # Store the session ID and username somewhere. In a real application,
        # you'd probably store this in a database. For simplicity, let's just
        # use a global dictionary.
        user_sessions[session_id] = username
    
        # Create a new response to send back
        response = make_response(render_template('welcome.html', username=username))
    
        # Set a cookie on the response
        response.set_cookie('session_id', session_id)
    
        return response
    else:
        return "Invalid credentials", 401
    
    
    @app.route('/logout', methods=['GET'])
    def logout():
    '''
    Log the user out by deleting their session ID.
    '''
    session_id = request.cookies.get('session_id')
    
    if session_id in user_sessions:
        del user_sessions[session_id]
    
    return "You have been logged out"
    
    
    # Create a global dictionary to store user sessions.
    # In a real application, you'd want to use a persistent database.
    user_sessions = {}
    
    
    