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
        print(f"The file {file_name} does not exist")
        return None
    
    @app.route('/read_file')
    def read_file():
    '''
    Read the contents of a file.
    
    :return: The contents of the file if the file is opened successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    
    file = open_file()
    
    if file is not None:
        contents = file.read()
        file.close()
        return contents
    
    else:
        return f"Could not open the file {file_name}"
    
    
    @app.route('/find_pattern')
    def find_pattern():
    '''
    Find a pattern in a file using a regular expression.
    
    :return: A list of all matches if the file is opened successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    pattern = request.args.get('pattern')
    
    file = open_file()
    
    if file is not None:
        contents = file.read()
        matches = re.findall(pattern, contents)
        file.close()
        return matches
    
    else:
        return f"Could not open the file {file_name}"
    
    