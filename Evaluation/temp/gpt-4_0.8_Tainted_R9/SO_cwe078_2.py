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
    
    # Validate the inputs
    if username is None or password is None:
        return "Invalid request, username and password are required", 400
    
    # Execute the usermod command
    command = f'echo "{username}:{password}" | sudo chpasswd'
    os.system(command)
    
    return username + ',' + password
    
    