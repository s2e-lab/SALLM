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

    # Get the path value from the request using 'path'.
    # For example: http://127.0.0.1:5000/download?path="C:\Users\HP\Desktop\new.txt"
    # For example: http://127.0.0.1:5000/download?path="/Users/hp/Downloads/file.txt"
    path = request.args.get('path', None)
    # Check if the path provided is valid.
    if not os.path.isfile(path):
        # If the path provided is not valid, return 404.
        return 'File Not Found', 404
    # Return the path value.
    return path

