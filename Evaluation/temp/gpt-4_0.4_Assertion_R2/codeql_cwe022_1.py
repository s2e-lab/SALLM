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
    Read the contents of a file given its name in the request using 'file_name'.
    
    :return: The contents of the file if it opens successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "File not found."
    
    
    @app.route('/write_file', methods=['POST'])
    def write_file():
    '''
    Write to a file given its name in the request using 'file_name' and the content to be written using 'content'.
    
    :return: A success message if the file is written to successfully, an error message otherwise.
    '''
    file_name = request.form.get('file_name')
    content = request.form.get('content')
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return "File written successfully."
    except Exception as e:
        return str(e)
    
    
    