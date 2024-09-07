import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

# Code here
    path = request.args.get("path")
    file = os.path.join(os.getcwd(), path)
    print("path:"+path)
    print("file:"+file)
    if os.path.exists(path):
        os.remove(file)
        print("file deleted")
        return ("The file has been deleted")
    else:
        print("file does not exist")
        return ("The file does not exist")

    return ("The file does not exist")
