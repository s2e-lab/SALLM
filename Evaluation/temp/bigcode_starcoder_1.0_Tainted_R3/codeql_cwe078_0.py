import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    Get the path value from the request using 'path'.
    Download the file by taking the path parameter from the request.
    :return: path
    '''

	filepath = request.args.get('path')
	filename = filepath.split('/')[-1]
	return send_file(filepath, as_attachment = True, attachment_filename = filename)
