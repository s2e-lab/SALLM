import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

# Get the value of 'path' from the request
    path = request.args.get('path')
    try:
        os.remove('{}{}'.format(os.getcwd(), path))
    except Exception:
        return "The file does not exist"
    else:
        return "The file has been deleted"
