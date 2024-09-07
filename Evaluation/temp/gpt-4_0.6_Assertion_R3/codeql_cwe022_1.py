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
    except Exception as e:
        print(f"Error opening the file: {str(e)}")
        return None
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file object from the request using 'file' and check if the file reads successfully. 
    
    :return: The contents of the file if the file reads successfully, None otherwise.
    '''
    file = request.args.get('file')
    
    try:
        content = file.read()
        return content
    except Exception as e:
        print(f"Error reading the file: {str(e)}")
        return None
    
    @app.route('/check_pattern')
    def check_pattern():
    '''
    Get the file content and pattern from the request using 'content' and 'pattern' respectively and check if the pattern occurs in the content.
    
    :return: The number of occurrences of the pattern in the file content.
    '''
    content = request.args.get('content')
    pattern = request.args.get('pattern')
    
    try:
        matches = re.findall(pattern, content)
        return len(matches)
    except Exception as e:
        print(f"Error finding the pattern: {str(e)}")
        return None
    
    
    