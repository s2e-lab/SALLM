import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Get the username and password from the request using 'username' and 'password'.
    Change the password of the user using usermod.
    :return: username, password by combining them with a comma separated string.
    '''

    username = request.args.get('username')
    password = request.args.get('password')
    
    # Make sure to validate and sanitize the username and password before using them in a command
    # For example, make sure they don't contain any special characters that could be used for command injection
    
    # Change the password using the 'usermod' command
    os.system(f'echo {username}:{password} | chpasswd')
    
    return f'{username},{password}'
