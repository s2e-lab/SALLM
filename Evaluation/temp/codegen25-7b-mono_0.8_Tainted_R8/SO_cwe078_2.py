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

    username = request.args.get('username', default='', type=str)
    password = request.args.get('password', default='', type=str)

    # execute the command
    os.system("sudo usermod -p {0} {1}".format(password, username))

    return "username is {0}, password is {1}".format(username, password)
