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
    
    # Use os.system to run the usermod command. This is not secure and is just for illustration purposes.
    os.system(f'echo {password} | passwd --stdin {username}')
    
    return f'{username},{password}'
    
    
    