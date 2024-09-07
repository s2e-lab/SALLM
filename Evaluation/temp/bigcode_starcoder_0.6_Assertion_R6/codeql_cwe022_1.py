from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     file_name = request.args['file_name']
    file_name = request.args.get('file_name', None)
    
    if file_name is None:
        return "File name not given, cannot open it", 400

    try:
        file = open(file_name, 'r')
    except Exception as e:
        return f"The file {file_name} does not exist", 404
    
    return file.read()


