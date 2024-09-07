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
    
    
    @app.route('/read_file', methods=['POST'])
    def read_file():
    """
    Read the content of a file and return it as a response.
    The file name should be sent in the request body as JSON
    
    :return: The content of the file as a response, or error message if the file does not exist.
    """
    
    file_name = request.json.get('file_name')
    
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return 'File does not exist'
    
    
    @app.route('/write_file', methods=['POST'])
    def write_file():
    '''
    Write a text to a file. The file name and the text should be sent in the request body as JSON
    
    :return: A success message if the operation was successful, or an error message otherwise.
    '''
    
    file_name = request.json.get('file_name')
    text = request.json.get('text')
    
    try:
        with open(file_name, 'w') as file:
            file.write(text)
        return 'Successfully written to file'
    except Exception as e:
        return f'An error occurred: {str(e)}'
    
    
    