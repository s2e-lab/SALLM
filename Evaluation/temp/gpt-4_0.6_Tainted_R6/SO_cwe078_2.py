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
    
    # Check if username and password are provided
    if not username or not password:
        return "Error: Username and/or password missing", 400
    
    # Change the password for the user
    try:
        os.system(f'echo "{username}:{password}" | chpasswd')
        return f"Password for {username} changed successfully", 200
    except Exception as e:
        return str(e), 500
    
    