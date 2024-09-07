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
    return '', 302, {'Location':<mask_1>.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'wasm')
        return send_from_directory(directory=filename, path='todos.wasm', download_name='todos.wasm')
