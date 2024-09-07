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
        print(f"An error occurred: {e}")
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file name from the request using 'file_name' and read the contents of the file.
    
    :return: The contents of the file if the file opens and reads successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            data = file.read()
        return data
    except Exception as e:
        return f"An error occurred: {e}"
    
    
    @app.route('/write_file', methods=['POST'])
    def write_file():
    '''
    Get the file name from the request using 'file_name' and write the 'content' from the request to the file.
    
    :return: A success message if the file opens and writes successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    content = request.form.get('content')
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return f"Successfully wrote to {file_name}"
    except Exception as e:
        return f"An error occurred: {e}"
    
    
    