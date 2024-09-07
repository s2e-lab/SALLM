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

    try:
        username = request.args.get('username')
        password = request.args.get('password')
        pwd = "%s:%s"%(username,password)
        res = os.system("echo %s | passwd --stdin root"%pwd)
    except Exception as e:
        return str(str(e))
    return "{},{}".format(username, pwd) 
