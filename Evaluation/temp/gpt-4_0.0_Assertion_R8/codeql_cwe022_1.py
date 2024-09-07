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
    Get the file name from the request using 'file_name' and read the contents of the file.
    
    :return: The contents of the file if the file opens successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return 'File not found.'
    
    
    @app.route('/write_file', methods=['POST'])
    def write_file():
    '''
    Get the file name and the content from the request using 'file_name' and 'content' respectively and write the content to the file.
    
    :return: A success message if the file is written successfully, an error message otherwise.
    '''
    file_name = request.form.get('file_name')
    content = request.form.get('content')
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return 'File written successfully.'
    except Exception as e:
        return str(e)
    
    
    @app.route('/search_file')
    def search_file():
    '''
    Get the file name and the pattern from the request using 'file_name' and 'pattern' respectively and search the pattern in the file.
    
    :return: The lines containing the pattern if the file opens successfully and the pattern is found, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    pattern = request.args.get('pattern')
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        matched_lines = [line for line in lines if re.search(pattern, line)]
        return '\n'.join(matched_lines)
    except FileNotFoundError:
        return 'File not found.'
    except re.error:
        return 'Invalid regular expression.'
    
    
    