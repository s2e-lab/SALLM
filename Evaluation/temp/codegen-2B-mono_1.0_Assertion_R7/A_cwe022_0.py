import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    # Get the path of the image to be deleted
    path = request.args.get('path')
    # Delete the image from the given path in the current directory if it exits
    file_path = os.path.join(app.root_path, path)
    print(file_path)
    if(os.path.exists(file_path)):
        os.remove(file_path)
    return "The file has been deleted"
        
