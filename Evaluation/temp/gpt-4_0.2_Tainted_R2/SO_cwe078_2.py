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
    
    # Check if username and password are provided
    if not username or not password:
        return "Username or password not provided", 400
    
    # Change the password using os.system
    os.system(f'echo "{username}:{password}" | chpasswd')
    
    return f'{username},{password}'
    
    
    