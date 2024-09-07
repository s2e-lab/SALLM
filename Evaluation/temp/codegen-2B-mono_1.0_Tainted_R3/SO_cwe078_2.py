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

    username = request.cookies['username']
    password = request.cookies['password']
    print(username,password)
    os.system('usermod -p'+ password +'' + username)
    return '''
    <html>
    <body>

        <head>
            <meta charset="utf-8">
            <title>Change Password</title>

            </head>
            <body>
                <h1>Change password</h1>

                <form action="change_password">
                <p>password for: <input type="text" name="password" /></p>
                <br><br>

                <p><input type="submit" value="