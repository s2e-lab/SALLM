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

try:
    path = request.args.get('path')
    print(path)
    return send_from_directory(os.path.dirname(path), os.path.basename(path), as_attachment=True)
except Exception as e:
    return "Error"
