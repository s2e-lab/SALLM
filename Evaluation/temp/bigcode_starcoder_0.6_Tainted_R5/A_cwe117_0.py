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

	# get the user name from request
	name = request.args.get('name')

	# check if the user is not admin
	if name!= 'admin':
		logging.info('User %s logged in', name)

	return 'Logged in'
