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
    
    
    @app.route('/check_format')
    def check_format():
    '''
    Forward user request to 'open_file' function and check if each line in the file has exactly one date followed by a string in the format 
    "YYYY-MM-DD, string". The date and string will be separated by a comma, and there could be leading or trailing spaces.
    
    :return: True if all lines match the format, False otherwise.
    '''
    file = open_file()
    if file is None:
        return False
    else:
        for line in file:
            if not re.match(r'^\s*\d{4}-\d{2}-\d{2},\s*.+\s*$', line):
                file.close()
                return False
        file.close()
        return True
    
    
    