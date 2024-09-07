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

	response = make_response(send_from_directory(request.args.get("path"), "file.pdf"))
	cd = 'attachment; filename=file.pdf'
	response.headers['Content-Disposition'] = cd
	return response
