import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

	# get the path to the html form
    file = request.args.get('path', '')
    try:
        os.remove(file);
        return "The file has been deleted"
    except OSError:
        return "The file does not exist"
