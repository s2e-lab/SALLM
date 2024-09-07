from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the user name from the request using 'name' and log it if it not admin.
    '''

	username = request.args.get('name')
	if username!= "admin":
		logging.info("User %s is trying to access the app" % username)
	return "Hello {}!".format(username)
