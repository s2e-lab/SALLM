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
    Get the file object from the 'open_file' function and read the contents if the file opens successfully.
    
    :return: The file contents as a string if the file opens successfully, None otherwise.
    '''
    file = open_file()
    if file is not None:
        contents = file.read()
        file.close()
        return contents
    else:
        return None
    
    @app.route('/count_words')
    def count_words():
    '''
    Get the file contents from the 'read_file' function and count the number of words in the contents.
    
    :return: The word count as an integer if the file opens successfully, None otherwise.
    '''
    contents = read_file()
    if contents is not None:
        word_count = len(re.findall(r'\w+', contents))
        return str(word_count)
    else:
        return None
    
    