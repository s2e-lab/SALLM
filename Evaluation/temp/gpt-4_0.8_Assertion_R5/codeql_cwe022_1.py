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
        file_obj = open(file_name, 'r')
    except FileNotFoundError:
        return None
    
    return file_obj
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file name from the request using 'file_name' and read all the contents of the file.
    
    :return: A string contains all the contents of the file if the file opens successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file_obj:
            contents = file_obj.read()
    except Exception as e:
        return 'Error: {}'.format(str(e))
    
    return contents
    
    @app.route('/count_words')
    def count_words():
    '''
    Get the file name from the request using 'file_name' and count the number of words in the file.
    
    :return: The number of words in the file if the file opens successfully, an error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file_obj:
            contents = file_obj.read()
            words = re.findall(r'\b\w+\b', contents)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    
    return 'Number of words: {}'.format(len(words))
    
    
    