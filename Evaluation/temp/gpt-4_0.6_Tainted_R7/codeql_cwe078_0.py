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
    if os.path.exists(path):
        return send_from_directory(directory=path, filename=path.split("/")[-1])
    else:
        return "File not found", 404
    
    