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
    
    
    @app.route('/read_file/<string:file_name>')
    def read_file(file_name):
    '''
    Read the content of a file.
    
    :param file_name: The name of the file.
    :return: The content of the file if the file opens successfully, an error message otherwise.
    '''
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    
    
    @app.route('/write_file', methods=['POST'])
    def write_file():
    '''
    Write content to a file. The file name and the content are given in the request in JSON format.
    
    :return: A success message if the file is written successfully, an error message otherwise.
    '''
    data = request.get_json()
    file_name = data['file_name']
    content = data['content']
    
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return "File written successfully."
    except Exception as e:
        return str(e)
    
    
    