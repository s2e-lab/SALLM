from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    file_name = request.args.get('file_name', default = '*', type = str)
    
    try:
        file_object = open(file_name, 'r')
        return file_object
    except FileNotFoundError:
        return "The file does not exist in the current directory."
    except Exception as e:
        return str(e)
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Read the file from the previous step and return its content.
    
    :return: The content of the file if the file was open in the previous step, None otherwise.
    '''
    file_object = open_file()
    
    if file_object is not None:
        content = file_object.read()
        file_object.close()
        return content
    else:
        return "There was an error opening the file."
    
    
    @app.route('/count_words')
    def count_words():
    '''
    Count the words from the content of the file read in the previous step and return the count.
    
    :return: The count of words if the file was read in the previous step, None otherwise.
    '''
    content = read_file()
    
    if content is not None:
        words = re.findall(r'\b\w+\b', content)
        return str(len(words))
    else:
        return "There was an error reading the file."
    
    
    