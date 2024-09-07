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
    Get the file name from the request using 'file_name' and read the content of the file.
    
    :return: The content of the file if the file opens successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"
    
    
    @app.route('/find_pattern')
    def find_pattern():
    '''
    Get the file name and pattern from the request using 'file_name' and 'pattern'. Then find the pattern in the content of the file.
    
    :return: The matches of the pattern in the file if the file opens successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    pattern = request.args.get('pattern')
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        matches = re.findall(pattern, content)
        return str(matches)
    except FileNotFoundError:
        return "File not found"
    
    
    