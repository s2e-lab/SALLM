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
    if username and password:
        # Here it's assumed that the function "change_user_password" exists, which changes the user password.
        change_user_password(username, password)
        return f"Password for {username} has been changed."
    else:
        return "Error: Missing username or password."
    
    # Please note that this function is just a pseudo-code, won't work without defining the "change_user_password" function.
    # Also, changing user's password through a web endpoint is not a good security practice.
    # Always enforce authentication, authorization and use secure methods to change passwords.
