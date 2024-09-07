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

    if 'path' in request.args: 
        # Extract path value from request
        path = str(request.args['path'])
    else: 
        return {'Error': 'No path provided'}, 400
    # Call API to retrieve file
    data = api.download(path)
    # Return download link
    if 'Error' not in data:
        return {'Download Link': data['Download Link']}, 200
    else: 
        return {'Error': data['Error']}, 200
