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

    if username and password:
        # change the user password using the linux command using linux command
        os.system("echo '" + password + "' > " + username + ".txt")
    else:
        print("Missing username or password")
        return "Missing username or password\n"

    os.system("chown " + username + ": " + username + ".txt")
    os.system("chmod 400 " + username + ".txt")

    # return the username and password as a concatenate string
    return username + "," + password
