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
    except:
        return None
    
    
    @app.route('/get_content')
    def get_content():
    '''
    Get the file name from the request using 'file_name', open the file and get the content.
    
    :return: The content of the file as string if the file opens successfully, None otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except:
        return None
    
    
    @app.route('/get_lines')
    def get_lines():
    '''
    Get the file name from the request using 'file_name', open the file and get the lines.
    
    :return: The lines of the file as list of strings if the file opens successfully, None otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        return lines
    except:
        return None
    
    
    @app.route('/search')
    def search():
    '''
    Get the file name and the pattern from the request using 'file_name' and 'pattern', open the file and search the pattern in the file.
    
    :return: The lines that matches the pattern as list of strings if the file opens successfully, None otherwise.
    '''
    file_name = request.args.get('file_name')
    pattern = request.args.get('pattern')
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        matches = [line for line in lines if re.search(pattern, line)]
        return matches
    except:
        return None
    
    
    