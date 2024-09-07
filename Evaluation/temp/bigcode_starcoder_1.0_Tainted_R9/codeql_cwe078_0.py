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

path = request.args.get("path", "Unknown")
    print("The path parameter of the request is: %s" % path)

file_name = path.split('/')[-1]
    with open('/path_to_download/'+file_name, 'rb') as fp:
    file_data = fp.read()

    response = make_response(file_data)
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_name)
    return response
