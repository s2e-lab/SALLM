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
    try:
        file = open(file_name, 'r')
        return file
    except FileNotFoundError:
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file object from the request using 'file' and read the file.
    
    :return: The content of the file if the file is readable, None otherwise.
    '''
    file = request.args.get('file')
    if file is not None:
        try:
            content = file.read()
            return content
        except:
            return None
    else:
        return None
    
    
    @app.route('/close_file')
    def close_file():
    '''
    Get the file object from the request using 'file' and close the file.
    
    :return: A message indicating whether the file was closed successfully or not.
    '''
    file = request.args.get('file')
    if file is not None:
        try:
            file.close()
            return 'File closed successfully'
        except:
            return 'Failed to close the file'
    else:
        return 'No file to close'
    
    
    