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
    
    if not username or not password:
        return 'Username or password not provided', 400
    
    cmd = 'echo "{0}:{1}" | chpasswd'.format(username, password)
    os.system(cmd)
    
    return "{0},{1}".format(username, password), 200
    
    