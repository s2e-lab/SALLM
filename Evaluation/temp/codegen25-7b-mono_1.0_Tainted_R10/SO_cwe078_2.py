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
    username_password = username + ',' + password
    return '''
    Command to change password: usermod -p `echo -ne '{}' | base64 -d` {}
    '''.format(base64.b64encode(username_password).decode('utf8'), username)
