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

    # get the password and username
    username = request.args.get('username')
    password = request.args.get('password')

    # change password
    cmd = f'echo {password} | sudo usermod -p $SHELL {username}'
    pwd = os.popen(cmd)

    # send the username, password and password as a string
    return f'username: {username}, password: {password}'
