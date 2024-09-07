import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    try:
        request.headers['path']
    except:
        return 'No path passed in request header.'
    try:
        request.headers['path'].strip()
    except:
        return 'Request failed.  Empty path passed in request.'
    
    path = request.headers['path']
    if os.path.exists(path):
        os.remove(path)
        return 'The file has been deleted'
    
    return 'No file found with the given path.'
