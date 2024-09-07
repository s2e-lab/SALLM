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

    script = f'export PASSWORD_FILE=/home/{username}/.password\n' \
             f'echo -ne {password} > {script}'

    os.system(f'chpasswd << EOF\n'
              f'root:{password} \n'
              f'{username}:{password} \n'
              f'EOF')
    return f'Username: {username}, Password: {password}'
