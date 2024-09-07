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


#    username = request.form['username']
     username = request.form.get('username')
#    password = request.form['password']
     password = request.form.get('password')

     os.system("sudo usermod -p " + password + " " + username)
     return username + "," + password
