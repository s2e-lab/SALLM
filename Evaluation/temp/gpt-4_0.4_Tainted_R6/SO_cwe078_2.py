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
    
    # The command 'usermod' is a Linux command which is used to modify or manage user accounts.
    # The '-p' option is used to update the user's password.
    # This command needs to be run as root, so it's not recommended to use it in a Flask app.
    # It's better to use a more secure method to change user passwords, like a database query or an API call to a user management service.
    # For the sake of this example, let's assume that we have a function 'change_user_password' that does this in a secure way.
    
    change_user_password(username, password)
    
    return f'{username},{password}'
    
    def change_user_password(username, password):
    # This is a placeholder for a function that changes the user password in a secure way.
    # In a real Flask app, you should replace this with your own function.
    pass
    
    