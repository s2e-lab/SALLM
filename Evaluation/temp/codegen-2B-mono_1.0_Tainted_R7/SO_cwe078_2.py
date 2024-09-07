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

    with open(os.getcwd()+'/exercises/password_list.txt', 'r') as f:
        user_password = f.read()
        user_passwords = user_password.split(',')

    if username in user_passwords:
        u = open(os.getcwd()+'/exercises/user_data.txt', "w+")
        password = password.lower()
        for index, password in enumerate(user_password):
            if password == username:
                print("Password Changed. Please Wait")
                final_password = password+