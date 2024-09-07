import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

	app.logger.setLevel(logging.DEBUG)
	app.logger.info("\n***\n" + "Logging request..." + "\n***\n")
	for header in request.headers:
		app.logger.info(header + ": " + request.headers[header])
	app.logger.info("\n***\n" + "Logging request done." + "\n***\n")
	return '\n'.join(sorted(request.headers))
