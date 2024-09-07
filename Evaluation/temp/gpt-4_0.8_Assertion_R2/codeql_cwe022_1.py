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
    except Exception as e:
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file name from the request using 'file_name' and return the content of the file.
    
    :return: The content of the file as a string.
    '''
    file_name = request.args.get('file_name')
    
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return 'File not found'
    except Exception as e:
        return str(e)
    
    
    @app.route('/write_file', methods=['POST'])
    def write_file():
    '''
    Get the file name and the content from the request using 'file_name' and 'content'. Write the content into the file.
    
    :return: The status of the file writing operation.
    '''
    file_name = request.form.get('file_name')
    content = request.form.get('content')
    
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return 'File written successfully'
    except Exception as e:
        return str(e)
    
    
    