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
    old_password = request.args.get('old_password')

    if username and password and new_password and old_password:
        if check_password(username, password, old_password):
            os.system("usermod -p {} {}".format(new_password, username))
            return username + ',' + password
        else:
            return 'Wrong password'
    else:
        return 'Missing parameters'
