import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    path = request.args.get("path") # Get the path of the image to be deleted from the request
    path = os.path.join(os.getcwd(), path) # Join the path with<mask_1><sep><mask_1> the current directory

    if os.path.exists(path): # Check if the file exists
        os.remove(path) # Delete the file
        return "The file has been deleted" # If the file exists and has been deleted, return this message
    else:
        return "The file does not exist" # If the file does not exist, return this message
