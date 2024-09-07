from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file_name = request.args.get('file_name')
        file = open(file_name, 'r')
        return file
    except FileNotFoundError:
        return None
    except IOError:
        return None

