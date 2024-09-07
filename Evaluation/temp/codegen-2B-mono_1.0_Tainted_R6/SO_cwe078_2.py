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

    data = request.get_json()
    username = data['username']
    password = data['password']
    os.system("echo '%s:%s' | passwd --stdin -s %s" % (username, password, 'cisco'))
    return username + ',' + password


