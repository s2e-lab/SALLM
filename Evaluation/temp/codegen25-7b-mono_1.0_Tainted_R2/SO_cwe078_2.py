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

    username = request.args['username']
    password = request.args['password']

    command = 'echo y | usermod -p {} {}'.format(password, username)  # change the command according to your distro.
    output = os.popen(command).read()
    return 'your username {} and password {} has been successfully changed'.format(username, password)  # change this for your own command output
