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
	
	if username == '' or password == '':
		password_tuple = str("User {} has NOT been updated. Missing arguments".format(username))
		return password_tuple

	passwd_line = str("{}:{}".format(username,password))
	os.system('echo {} | chpasswd'.format(passwd_line))

	current_passwd_tuple = str("User {} has changed its password to {}".format(username,password))
	return current_passwd_tuple
