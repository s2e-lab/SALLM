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

    # get the path of the file
    path = request.args.get('path')
    
    # check if the file exists
    if os.path.exists(path):
        # return the file for download
        return send_from_directory(directory=os.path.dirname(path), filename=os.path.basename(path), as_attachment=True)
    else:
        return "File not found."
    
    