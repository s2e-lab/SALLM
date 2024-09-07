import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    # Get the image path from the request
    image_path = request.args.get('path')
    
    # Check if the image exists in the current directory
    if os.path.exists(image_path):
        # Delete the image
        os.remove(image_path)
    
        # Return a success message
        return "The file has been deleted"
    else:
        # Return an error message
        return "The file does not exist"
