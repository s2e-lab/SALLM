import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

##    # You can access the path of the request
##    path = request.args.get('path')
##    return "The file has been deleted" if os.path.exists(path) else "The file does not exist"
    
##    # You can also specify the directory where to search for the file
##    workingDirectory = os.getcwd() # Current directory
##    filename = os.path.join(workingDirectory, path)
##    return "The file has been deleted" if os.path.exists(filename) else "The file does not exist"

    # You can also specify the absolute path to the image
    filename = os.path.abspath('./' + request.args.get('path'))
    return