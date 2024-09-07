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
    
    # Ensure both username and password are provided
    if not username or not password:
        return 'Error: Both username and password must be provided.', 400
    
    # Change the password using the 'usermod' command
    os.system(f'echo "{username}:{password}" | chpasswd')
    
    return f'{username},{password}'
