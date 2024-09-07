import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    path=request.args.get("path")   #request.args.get("path") is the url address of the file

    #check if the file exists on the given path

    if os.path.isdir(path):   #check if the path provided by user exists in the server or not
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path,file)):
                try:    #check if a file directory is not empty
                    os.listdir(os.path.join(path,file))
                except:    #if it is empty, delete it
                    os.rmd