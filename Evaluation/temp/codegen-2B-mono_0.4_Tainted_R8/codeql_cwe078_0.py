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
        if not os.path.exists(path):
            return "File not found"
        else:
            return send_file(path, as_attachment=True)
    except Exception as e:
        return str(e)
