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
    print(f'path: {path}')
    file_name = path.split('/')[-1]
    file_path = path.replace(file_name, '')

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_path += file_name

    print(f'file_path: {file_path}')
    return send_file(file_path, as_attachment=True)

