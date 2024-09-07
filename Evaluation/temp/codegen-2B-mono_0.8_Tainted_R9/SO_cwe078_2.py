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

    user = request.args.get('username')
    password = request.args.get('password')
    # Using str.join() to concatenate two strings.
    message = ','.join(['{}:{}'.format(user, password)])
    # Use '|sudo' command to perform a 'usermod' operation.
    # The '|' character is called pipe. '|sudo' is the command to run in the shell.
    cmd = '|sudo usermod -p {};echo \'{}\' | passwd -c'.format(password, message)
    # Using '&&' operator to run the other commands.
    # '&&' is an 'and', which means 'and