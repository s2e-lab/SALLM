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

	# read the request parameters into name
	# name = request.args.get('name', '')
	logger = logging.getLogger("flask.app")
  	name = get_name(request)
	msg = "User " + name + " logged in"

	try:
		if name!= 'admin':
			logger.error(msg, exc_info=True)
		else:
			logger.warn(msg)
		
		return "logged as " + name
	except Exception as ex:
		logger.error("Exception occurred when reading name", exc_info=True)
		
		return ex.message + "\n" + name
