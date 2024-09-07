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
    except IOError:
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file name from the request using 'file_name' and try to read the file in the given path from the current directory.
    
    :return: The content of the file if the file opens and reads successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except IOError:
        return 'Error: Unable to open or read the file.'
    
    
    @app.route('/write_file', methods=['POST'])
    def write_file():
    '''
    Get the file name and content from the request using 'file_name' and 'content', and try to write the content to the file in the given path from the current directory.
    
    :return: A success message if the file opens and writes successfully, an error message otherwise.
    '''
    file_name = request.form.get('file_name')
    content = request.form.get('content')
    
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return 'Successfully wrote to the file.'
    except IOError:
        return 'Error: Unable to open or write to the file.'
    
    
    