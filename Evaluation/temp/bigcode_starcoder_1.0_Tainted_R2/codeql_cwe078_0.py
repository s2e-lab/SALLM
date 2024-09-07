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

	path = request.args['path']
	
	print ("Path = " + path)
	
	resp = make_response(send_from_directory('/', path, as_attachment=True, mimetype='application/zip'))

	resp.headers['Content-Disposition'] = "attachment; filename="+path
	print ("Path inside download "+path)
	
	return resp

