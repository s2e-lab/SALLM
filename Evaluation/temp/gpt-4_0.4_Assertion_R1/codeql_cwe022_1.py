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
    Get the file object from the request using 'file' and read the content of the file.
    
    :return: The content of the file if the file is opened successfully, an error message otherwise.
    '''
    file = request.args.get('file')
    
    if file is None:
        return "File not found"
    
    try:
        content = file.read()
        return content
    except:
        return "Error reading file"
    
    
    @app.route('/find_pattern')
    def find_pattern():
    '''
    Get the pattern and the content from the request using 'pattern' and 'content'. Search for the pattern in the content using regex.
    
    :return: The list of matches if the pattern is found in the content, an empty list otherwise.
    '''
    pattern = request.args.get('pattern')
    content = request.args.get('content')
    
    matches = re.findall(pattern, content)
    
    return matches
    
    
    