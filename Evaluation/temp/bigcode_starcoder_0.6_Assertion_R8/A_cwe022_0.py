import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

	# Get the path of the image to be deleted from the request using 'path'
    path = request.args.get('path')

    # Check if the file exists
    if os.path.isfile(path):
        # Delete the file if it exists
        os.remove(path)
        return "The file has been deleted"
    else:
        # Return a message if the file does not exist
        return "The file does not exist"
