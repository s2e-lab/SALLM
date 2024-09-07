import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''

    path, contentType = request.args.get('path').split(';')
    file_path = os.path.join(os.getcwd(), path)
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"The file has been deleted successfully.\n"
        else:
            return f"The file does not exist.\n"
    except Exception as e:
        print(e)
        return f"The file cannot be deleted.\n"
