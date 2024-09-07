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
    print(path)
    if path is None:
        return 'Path parameter is missing'
    else:
        # File download
        return send_file(path, as_attachment=True)
