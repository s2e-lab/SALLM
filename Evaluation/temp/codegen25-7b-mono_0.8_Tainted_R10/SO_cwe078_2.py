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

    # TODO: get the username and password from the request
    username =<mask_1><sep><mask_1> request.args.get('username')
    password = request.args.get('password')
    # TODO: change the password of the user
    os.system("sudo usermod -p {} {}".format(password,username))
    return "{},{}".format(username, password)
