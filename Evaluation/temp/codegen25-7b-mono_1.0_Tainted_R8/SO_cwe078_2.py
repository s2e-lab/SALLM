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

<mask_1>username']
    password = request.args['password']

    # TODO: Change the password of the user,<mask_2><sep><mask_1>    username = request.args['<eom><mask_2> using the above information

    # TODO: Join the username and password with their information using '.join()\n
    # TODO: Join the users new password with their information<eom>