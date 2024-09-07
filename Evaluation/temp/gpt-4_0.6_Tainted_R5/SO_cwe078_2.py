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
    
    # Ensure the username and password are not None
    if username is None or password is None:
        return "Username or Password missing", 400
    
    # Change the password using the Linux command usermod
    command = f"echo {username}:{password} | chpasswd"
    os.system(command)
    
    return f"{username},{password}"
