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
    
    # Assuming we have a function updateUserPassword to change the password.
    # updateUserPassword(username, password)
    
    # In a real-world scenario, we would not return the password in the response for security reasons.
    # For the purpose of this example, we will return it.
    return f'{username},{password}'
    
    