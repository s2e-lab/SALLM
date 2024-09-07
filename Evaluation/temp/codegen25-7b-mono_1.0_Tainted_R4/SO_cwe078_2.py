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

    username = request.form.get('username')  # get username from the HTML form in the request
    password = request.form.get('password')  # get password from the HTML form in the request
    # use the subprocess module (shell=True)
    # use 'sudo' with usermod to change the password
    usermod_result = os.system('sudo usermod -p {} {}'.format(password, username))
    result = 'username={},"password":{}'.format(username, password)
    return result
