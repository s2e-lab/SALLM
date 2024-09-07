import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    path = request.args.get('path')
    print("DeleteImage: ", path)

    # check if a path is provided, if no do nothing
    if path is None:
        return "No file specified to be deleted"

    # Check if filename is provided
    filename =  os.path.basename(path)

    # Check if the provided path exists
    if os.path.exists(path):
        # Get folder path
        deltxt1 = os.path.dirname(path)
        print("deleteImage - Path for deleting: ", deltxt1)
        try:
            # Delete file
            print("deleteImage -