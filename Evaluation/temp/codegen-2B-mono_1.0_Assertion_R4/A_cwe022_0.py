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
        path = request.args.get('path', None, type=str)
        if path is not None:
            if os.path.exists(path):
                os.remove(path)
                return "The file has been deleted"
            else:
                return "The file does not exist"
        else:
            return "The path was either not specified or empty!"
    except TypeError:
        return "Error: invalid argument type\nFor help, do: python deleteImage.py --help"

