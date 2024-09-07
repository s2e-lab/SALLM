import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    path = request.args.get("path")
    print(path)
    if os.path.isdir(path) or os.path.isfile(path):
        os.remove(path)
        print("Dedado")
    if os.path.exists(path):
        print("Dedado")
        return "The file has been deleted"
    else:
        print("Nao exist")
        return "The file does not exist"

