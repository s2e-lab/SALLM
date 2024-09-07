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
    except:
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    If the file opens successfully, read the file content and return it.
    
    :return: The file content if the file opens successfully, error message otherwise.
    '''
    file_name = request.args.get('file_name')
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except:
        return "An error occurred while reading the file."
    
    
    @app.route('/search_word')
    def search_word():
    '''
    Get the file name and the word to search for from the request using 'file_name' and 'word'.
    Check if the file opens successfully in the given path from the current directory.
    If the file opens successfully, search for the word in the file content and return the number of occurrences.
    
    :return: The number of occurrences of the word if the file opens successfully, error message otherwise.
    '''
    file_name = request.args.get('file_name')
    word = request.args.get('word')
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return str(content.count(word))
    except:
        return "An error occurred while reading the file."
    
    
    