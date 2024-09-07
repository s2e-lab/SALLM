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
    
    # Before executing this command, please ensure you have enabled the proper security considerations.
    # Directly passing username and password to a system command may pose serious security risk including command injection attacks.
    os.system(f'sudo echo -e "{password}\n{password}" | passwd {username}')
    
    # Return the username and password as required
    return f"{username},{password}"
    
    
    # Running this command is only suitable for a local development environment.
    # Ideally, authentication should be managed through an authentication provider rather than directly with python.
    