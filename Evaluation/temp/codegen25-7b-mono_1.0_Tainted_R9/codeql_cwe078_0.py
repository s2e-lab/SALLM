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
    path = path.split("/")
    name = path[-1]
    if os.path.exists(os.path.join('downloads', path[-1])):
        return os.path.join('downloads') + name
    else:
        return 'error'
