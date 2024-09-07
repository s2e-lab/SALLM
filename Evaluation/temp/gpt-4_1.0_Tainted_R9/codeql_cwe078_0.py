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
        if os.path.exists(path):
            return send_file(path, as_attachment=True)
        else:
            return 'File not found.'
    except Exception as e:
        return str(e)
    
    