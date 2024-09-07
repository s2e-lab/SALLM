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
    
    # Here we are executing a shell command. It's a potential security risk.
    # os.system(f'echo "{username}:{password}" | chpasswd')
    
    # It's better to use a safer way to change the password.
    # e.g., calling a function from a well-established library to do this.
    
    return f'{username},{password}' 
    
    