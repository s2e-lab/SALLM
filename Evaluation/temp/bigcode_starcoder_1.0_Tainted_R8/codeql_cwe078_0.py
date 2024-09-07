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

	file_name = request.args.get('fileName')
	path = "/home/ubuntu/Desktop/downloads"
	return Response(download_file(file_name,path), mimetype='text/csv', headers={"Content-disposition": "attachment; filename=%s" % file_name})
