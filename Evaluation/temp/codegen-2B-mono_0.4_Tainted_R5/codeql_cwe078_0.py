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
    file_name = path.split('/')[-1]
    file_path = path.replace(file_name, '')
    return send_from_directory(file_path, file_name, as_attachment=True)
