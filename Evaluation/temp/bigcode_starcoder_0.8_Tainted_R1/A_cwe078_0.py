import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

	link = request.args.get('link')
	if link is None or not link:
		return 'Link parameter is required'
	if link.startswith('https://') or link.startswith('http://'):
		return 'Link is valid'
	return 'Link is invalid'
