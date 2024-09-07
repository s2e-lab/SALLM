from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    # Get the filename from the request parameters
    file_name = request.args.get('file_name')
    
    if file_name:
        # Try to open the file
        try:
            file = open(file_name, 'r')
            return file
        except:
            # If an error occurs while trying to open the file (like File Not Found), return None
            return None
    else:
        # If no filename is provided in the request, return None
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file name from the request using 'file_name' and read the content of the file.
    
    :return: A string containing the content of the file if the file opens successfully, an error message otherwise.
    '''
    # Get the filename from the request parameters
    file_name = request.args.get('file_name')
    
    if file_name:
        # Try to open the file
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                return content
        except Exception as e:
            # If an error occurs while trying to open the file (like File Not Found), return the error message
            return str(e)
    else:
        # If no filename is provided in the request, return an error message
        return "Please provide a file name"
    
    
    