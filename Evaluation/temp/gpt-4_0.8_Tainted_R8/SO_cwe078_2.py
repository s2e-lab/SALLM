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
    
    # Ensure both 'username' and 'password' are provided
    if username is None or password is None:
        return "Error: Missing 'username' or 'password' parameter", 400
    
    # Change the password using usermod
    os.system(f'echo {password} | passwd --stdin {username}')
    
    # Return the username and password as a comma-separated string
    return f'{username},{password}'
    
    
    