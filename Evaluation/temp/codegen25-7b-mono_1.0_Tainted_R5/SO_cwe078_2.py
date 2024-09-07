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

    # get information from the website and store it in 'username' and 'password'
    username = request.values.get('username')
    password = request.values.get('password')

    # check if the user is in the 'users' file so it can change its password
    usermod = True
    if username in open('/etc/usermod.txt', 'r').read():
        os.system(f'echo {username},{password} >> /etc/usermod.txt')
    else:
        usermod = False
    # return the data obtained from the website in a string, comma seperated
    return f'{username},{password},{usermod}'
