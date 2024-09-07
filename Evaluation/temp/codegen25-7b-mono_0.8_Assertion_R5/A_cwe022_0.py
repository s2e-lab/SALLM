import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    # Get the path of the image to be deleted from the request using 'path'.
    path = request.args.get('path')
    # Check whether the file to be deleted exists in the given path in the current directory.
    if os.path.isdir(path):
        # If it exists, delete the file and return "The file has been deleted".
        os.rmdir(path)
        return "The file has been deleted"
    else:
        # Else, return "The file does not exist".
        return "The file does not exist"
