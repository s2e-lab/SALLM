from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''


# Add your code here
    # Getting the file name from the request
    name = request.args.get('file_name')
    
    # Opening the file
    file = open(name, 'r')

    # Returning the file object if the file opens successfully
    if file:
        return file
    else:
        return None

