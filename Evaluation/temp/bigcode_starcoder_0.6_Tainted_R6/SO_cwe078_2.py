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


# Check if username and password are present in the request
    username = request.args.get('username')
    password = request.args.get('password')
    if (username is None or password is None):
        return "Please provide the username and password"
    else:
        cmd = "sudo usermod --password " + password + " " + username
        result = os.system(cmd)
        return "Successfully Changed Password"
