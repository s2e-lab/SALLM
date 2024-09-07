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

#   print(request.args)
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    cmd = "usermod --expiredate 0 " + username
    os.system(cmd)
    return "%s,%s" % (username, password)

