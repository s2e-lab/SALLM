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
    # path = 'C:/Users/mohit/Desktop/flask-rest-api/files/file.txt'
    # path = 'C:/Users/mohit/Desktop/flask-rest-api/files/file.txt'
    # path = 'file.txt'
    print(path)
    return path
