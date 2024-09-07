import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    # Get the path of the image to be deleted from the request
    path = request.args.get('path')
    
    # Check if the file exists in the given path
    if os.path.exists(path):
        # Delete the file from the given path
        os.remove(path)
        
        return "The file has been deleted"
    else:
        return "The file does not exist"
