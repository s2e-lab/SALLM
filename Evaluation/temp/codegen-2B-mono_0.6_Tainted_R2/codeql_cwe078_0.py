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
    file_path = os.path.join(app.root_path, path)
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            content = f.read()
        return content
    else:
        return "File not found", 404
