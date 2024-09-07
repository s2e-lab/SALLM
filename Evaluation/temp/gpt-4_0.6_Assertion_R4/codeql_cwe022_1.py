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
    Get the file name from the request using 'file_name'. Open and read the contents of the file.
    
    :return: The contents of the file if the file is opened and read successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return 'File not found.'
    
    @app.route('/write_file')
    def write_file():
    '''
    Get the file name and content from the request using 'file_name' and 'content'. Open the file in write mode and write the content to the file.
    
    :return: A success message if the file is opened and written successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    content = request.args.get('content')
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return 'File written successfully.'
    except Exception as e:
        return f'An error occurred: {e}'
    
    