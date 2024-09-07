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
    resp = send_from_directory(directory='output', filename=path, as_attachment=True)
    resp.headers["Download"] = f"/download/{path}"
    return resp
