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


#    password = request.form['password']
#    username = request.form['username']
    password = '<PASSWORD>'
    username='change_passwd'
    pwd = 'password'
    os.system("usermod -p '{0}' {1}".format(password, username))
    return "{0},{1}".format(username, pwd)
