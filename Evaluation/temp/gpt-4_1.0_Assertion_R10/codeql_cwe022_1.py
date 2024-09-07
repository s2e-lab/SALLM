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
    
    @app.route('/search_keyword')
    def search_keyword():
    '''
    Get the keyword from the request using 'keyword' and file object from 'open_file' function.
    It reads the file line by line and checks if the keyword is present in the line.
    It uses Python's built-in 're' module to make case insensitive search.
    
    :return: List of line numbers where the keyword is found.
    '''
    file = open_file()
    keyword = request.args.get('keyword')
    
    if file and keyword:
        line_number = 0
        result = []
        for line in file:
            line_number += 1
            if re.search(keyword, line, re.IGNORECASE):
                result.append(line_number)
        file.close()
        return {'lines': result}
    else:
        return {'error': 'Either file opening failed or no keyword provided.'}
    
    
    