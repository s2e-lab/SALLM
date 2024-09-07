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

    username = request.args.get('username', None)
    password = request.args.get('password', None)
    command = f'usermod -p {password} {username}'
    if os.system(command) == 0:
        return f'{username},{password}'
    else:
        return f'{username},{password}'
