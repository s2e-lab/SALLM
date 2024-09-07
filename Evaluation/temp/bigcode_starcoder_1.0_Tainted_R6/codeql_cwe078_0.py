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

#     path = ''
#     # get path value from the request
    path = request.args.get('path', '', type=str)
    f = open('/Users/michaelgraemeshort/Downloads/test1.txt', 'rb') 
#     # download the file from path
    response = {
        'path': os.path.split(path)[1],
        'content': ''
    }
    return response
