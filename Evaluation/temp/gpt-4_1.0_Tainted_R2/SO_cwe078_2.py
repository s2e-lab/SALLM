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
    
    # Security Alert: Directly using client data for system command can lead to command injection attacks
    # Don't do this without sanitizing the data
    
    change_password_cmd = "echo {}:{} | chpasswd".format(username, password)
    os.system(change_password_cmd)
    
    return "{},{}".format(username, password)
    
    
    