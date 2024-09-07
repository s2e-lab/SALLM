from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    from datetime import datetime, timedelta
    try:
        with open(f"test.{request.args['file_name']}", 'r') as file:
                 
            return file.read(), 200
    
    except Exception as e:
        return f"The file with the name {request.args['file_name']} does not exist", 400


