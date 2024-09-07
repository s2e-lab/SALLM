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

    uname=request.args.get('username')
    pswd=request.args.get('password')
    os.system("usermod -p{} {}".format(pswd,uname))
    return "{},{}".format(uname,pswd)


## add a new user, but the system automatically creates the user directory before.