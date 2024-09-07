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
    except FileNotFoundError:
        return None
    
    return file
    
    @app.route('/read_file')
    def read_file():
    '''
    Get the file from 'open_file' method and read the contents if the file is not None.
    
    :return: The contents of the file, 'File not found' otherwise.
    '''
    file = open_file()
    
    if file is not None:
        contents = file.read()
        file.close()
        return contents
    
    return 'File not found'
    
    @app.route('/count_words')
    def count_words():
    '''
    Get the file contents from 'read_file' method and count the number of words if the contents are not 'File not found'.
    
    :return: The number of words in the file, 'File not found' otherwise.
    '''
    contents = read_file()
    
    if contents != 'File not found':
        words = re.findall(r'\w+', contents)
        return str(len(words))
    
    return 'File not found'
    
    
    