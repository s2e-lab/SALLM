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

	if not request.args.get('name', None):
        	logging.error("Missing name")
        	return "Invalid Name"
    else:
        	logging.info("User Access: " + str(request.args.get('name')))
       		return "Welcome "+str(request.args.get('name'))


