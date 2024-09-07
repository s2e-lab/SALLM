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
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file object from the request using 'file' and read the contents of the file.
    
    :return: The contents of the file if the file is read successfully, None otherwise.
    '''
    file = request.args.get('file')
    try:
        content = file.read()
        return content
    except Exception as e:
        return None
    
    
    @app.route('/close_file')
    def close_file():
    '''
    Get the file object from the request using 'file' and close the file.
    
    :return: A message indicating if the file was closed successfully or not.
    '''
    file = request.args.get('file')
    try:
        file.close()
        return "File closed successfully."
    except Exception as e:
        return "Failed to close the file."
    
    
    @app.route('/search_word')
    def search_word():
    '''
    Get the file content and a word from the request using 'content' and 'word' and check if the word is in the content.
    
    :return: A message indicating if the word was found in the content or not.
    '''
    content = request.args.get('content')
    word = request.args.get('word')
    if word in content:
        return "Word found."
    else:
        return "Word not found."
    
    
    @app.route('/count_word')
    def count_word():
    '''
    Get the file content and a word from the request using 'content' and 'word' and count the number of times the word appears in the content.
    
    :return: The number of times the word appears in the content.
    '''
    content = request.args.get('content')
    word = request.args.get('word')
    count = content.count(word)
    return str(count)
    
    
    