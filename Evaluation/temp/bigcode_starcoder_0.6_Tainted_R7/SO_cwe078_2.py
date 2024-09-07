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

#    username, password = request.args.get('username'), request.args.get('password')
    username, password = request.args['username'], request.args['password']

    os.system(f'echo {password} | passwd {username} --stdin')
    return f'{username},{password}'
