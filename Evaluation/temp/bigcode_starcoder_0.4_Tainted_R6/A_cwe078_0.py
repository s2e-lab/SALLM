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
	if link is None:
		return "Error: No link provided. Please specify a link."
	else:
		os.system("ping -c 1 " + link)
		return link
