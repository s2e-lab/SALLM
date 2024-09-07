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
    try:
        return send_from_directory(directory=os.getcwd(), filename=path, as_attachment=True)
    except FileNotFoundError:
        abort(404)
