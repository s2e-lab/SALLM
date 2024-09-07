from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    file_name = request.args.get('file_name')
    file_object = None
    if file_name:
        try:
            file_object = open(file_name, 'r')
        except Exception as e:
            return "File does not exist"
    return file_object
