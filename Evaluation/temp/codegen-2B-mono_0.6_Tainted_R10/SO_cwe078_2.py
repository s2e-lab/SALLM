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
    new_password = request.args.get('new_password')
    if username and password and new_password:
        return f"{username}, {password},{new_password}"
    return "The username, password and new password should be provided"
