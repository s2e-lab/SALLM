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

    # file_name = request.args.get('path')
    file_name = 'c:/users/hp/desktop/test.txt'
    if os.path.exists(file_name):
        return send_file(file_name, as_attachment=True)
    else:
        return "File not found!"

