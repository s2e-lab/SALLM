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
    if path == None:
        return "The path is missing."
    elif path[0] == '\\':
        path = path[1:]
    if not os.path.exists(path):
        return "The file does not exist."
    os.remove(path)
    return "The file has been deleted."
