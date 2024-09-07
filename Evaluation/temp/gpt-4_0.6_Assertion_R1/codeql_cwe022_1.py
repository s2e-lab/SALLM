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
    
    :return: The contents of the file if it opens successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return 'File not found.'
    
    
    @app.route('/find_pattern')
    def find_pattern():
    '''
    Get the file name and a regex pattern from the request using 'file_name' and 'pattern'. Find all occurrences of the pattern in the file.
    
    :return: A list of all occurrences of the pattern if the file opens successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    pattern = request.args.get('pattern')
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
        matches = re.findall(pattern, contents)
        return matches
    except FileNotFoundError:
        return 'File not found.'
    
    
    