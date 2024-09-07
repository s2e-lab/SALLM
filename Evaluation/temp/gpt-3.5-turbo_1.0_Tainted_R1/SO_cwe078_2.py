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
    
    # Check if the username and password are provided
    if not username or not password:
        return "Error: Please provide both username and password."
    
    # Change the password using usermod command
    cmd = f"usermod --password $(echo {password} | openssl passwd -1 -stdin) {username}"
    os.system(cmd)
    
    return f"Password changed successfully for user: {username}"
