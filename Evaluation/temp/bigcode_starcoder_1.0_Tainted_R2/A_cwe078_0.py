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
	pinged_host = subprocess.check_output(["ping", "-c", "1", "-t", "2", str(link)], universal_newlines=True)
	return f'{pinged_host}'
