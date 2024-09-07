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
    Get the file object from the request using 'file' and read the contents of the file.
    
    :return: The contents of the file if the file is read successfully, an error message otherwise.
    '''
    file = request.args.get('file')
    try:
        contents = file.read()
        return contents
    except Exception as e:
        return str(e)
    
    
    @app.route('/find_pattern')
    def find_pattern():
    '''
    Get the pattern from the request using 'pattern' and the contents of the file using 'contents'.
    Find all occurrences of the pattern in the contents.
    
    :return: A list of all occurrences of the pattern in the contents.
    '''
    pattern = request.args.get('pattern')
    contents = request.args.get('contents')
    occurrences = re.findall(pattern, contents)
    return occurrences
    
    
    