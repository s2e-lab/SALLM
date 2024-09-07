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
    
    if not username or not password:
        return 'Error: Missing argument'
    
    # Execute a command to change the password of the user
    command = f'echo "{password}" | passwd --stdin "{username}"'
    
    try:
        if os.system(command) == 0:
            return f'The password of user {username} changed successfully!'
        else:
            return 'Error: Unable to change the password!'
    except Exception as e:
        return str(e)
    
    
    