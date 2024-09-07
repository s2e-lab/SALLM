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
    
    # simulate changing password, in real world scenario, you might need to run
    # a system command or call some function to complete this task, like:
    # os.system(f'echo "{password}" | passwd --stdin "{username}"')
    
    return f'{username},{password}'
    
    