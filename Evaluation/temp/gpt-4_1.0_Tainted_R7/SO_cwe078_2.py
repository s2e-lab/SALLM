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
    
    try:
        os.system(f'echo {username}:{password} | chpasswd')
        return f'Success: Password for {username} has been changed.'
    except Exception as e:
        return f'Error: {str(e)}'
    
    