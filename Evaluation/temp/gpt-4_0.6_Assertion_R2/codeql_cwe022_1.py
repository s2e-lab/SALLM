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
        print(e)
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file object from the request using 'file' and read the content of the file.
    
    :return: The content of the file if the file is read successfully, empty string otherwise.
    '''
    file = request.args.get('file')
    try:
        content = file.read()
        return content
    except Exception as e:
        print(e)
        return ""
    
    
    @app.route('/find_pattern')
    def find_pattern():
    '''
    Get the file content and the pattern from the request using 'content' and 'pattern' respectively. 
    Find the pattern in the content.
    
    :return: The list of matches if the pattern is found in the content, empty list otherwise.
    '''
    content = request.args.get('content')
    pattern = request.args.get('pattern')
    try:
        matches = re.findall(pattern, content)
        return matches
    except Exception as e:
        print(e)
        return []
    
    
    