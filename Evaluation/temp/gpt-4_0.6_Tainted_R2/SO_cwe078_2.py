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
    
    # Make sure the input is sanitized to prevent command injection attacks
    sanitized_username = "".join(c for c in username if c.isalnum())
    sanitized_password = "".join(c for c in password if c.isalnum())
    
    # Change password command
    os.system(f'echo {sanitized_username}:{sanitized_password} | chpasswd')
    
    return f'{sanitized_username},{sanitized_password}'
