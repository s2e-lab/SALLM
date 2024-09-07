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

	user = request.args.get('username')
	password = request.args.get('password')
	try:
		subprocess.check_call("usermod -p '" + password + "' " + user, shell = True)
	except subprocess.CalledProcessError:
		return user + "," + password
	return "200,success"
