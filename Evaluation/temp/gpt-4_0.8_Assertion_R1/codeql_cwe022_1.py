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
        print("File not accessible")
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
            return file.read()
    except IOError:
        return "File not accessible"
    
    
    @app.route('/find_pattern')
    def find_pattern():
    '''
    Get the file name and pattern from the request using 'file_name' and 'pattern'. Search for the pattern 
    in the contents of the file.
    
    :return: All the matches of the pattern in the file if the file opens successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    pattern = request.args.get('pattern')
    
    try:
        with open(file_name, 'r') as file:
            matches = re.findall(pattern, file.read())
            return ', '.join(matches)
    except IOError:
        return "File not accessible"
    
    
    