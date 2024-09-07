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

    path = request.args.get('path')
    
    # Create the path to the file in the server.
    filename = 'download.csv'

    # Check if the file exists in the server.
    if os.path.exists(filename):
        return send_file(filename)
    else:
        return "File does not exist"
