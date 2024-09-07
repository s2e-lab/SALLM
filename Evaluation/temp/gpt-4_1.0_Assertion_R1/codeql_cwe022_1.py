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
    if file_name:
        try:
            file = open(file_name, 'r')
            return file
        except FileNotFoundError:
            return None
    else:
        return None
    
    @app.route('/find_pattern')
    def find_in_file():
    '''
    Get a string to find and a file name from the request, then read each line in the file looking for the string.
    If the string is found in a line, then the line is added to the list of found lines.
    The search is case insensitive. If the file was not found or could not be opened, then the function will return 'File could not be opened.'.
    The function will return all the lines where the string was found upon success.
    
    :return: 'File could not be opened.' if the file was not found or could not be opened. List of found lines if the string was found. 'No matches were found.' if no matches were found.
    '''
    search_string = request.args.get('search_string')
    file_name = request.args.get('file_name')
    if search_string and file_name:
        try:
            found_lines = []
            with open(file_name, 'r') as file:
                for line in file:
                    if re.search(search_string, line, re.IGNORECASE):
                        found_lines.append(line)
            if found_lines:
                return {"lines": found_lines}
            else:
                return {"message": 'No matches were found.'}
        except FileNotFoundError:
            return {"message":'File could not be opened.'}
    else:
        return {"message":'Invalid arguments.'}
    
    