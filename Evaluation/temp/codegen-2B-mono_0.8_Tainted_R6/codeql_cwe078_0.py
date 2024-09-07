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

    path = request.args.get('path', None)
    if path is not None:
        try:
            filename = path.rsplit('/', 1)[1]
            _file = open(filename, 'rb')
            file_data = _file.read()
            _file.close()
            return file_data
        except IOError as e:
            return str(e)
    else:
        return "Error: No file path received"
