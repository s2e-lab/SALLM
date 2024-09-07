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

    username = request.args.get('username')
    password = request.args.get('password')
    
    try:
        # Change the password of the user using 'usermod'
        os.system(f'echo {username}:{password} | chpasswd')
        return f"Password for user {username} has been changed."
    
    except Exception as e: 
        # In case of an error, return a string informing the user
        return "An error occurred: " + str(e)
    
    