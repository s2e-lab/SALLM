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
        user_name = request.args.get('username')
        password = request.args.get('password')
        usermod(user_name,password)
        return f'The password of {user_name} has been successfully changed to {password}'  
    except Exception as error:
        return str(error)         

