from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    file_path = request.values.get('file_name')
    try:
        file_object = open(file_path, 'r')
        return file_object
    except IOError:
        return None


