from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    # Read the file name from the request's body.
    file_name = request.args.get('file_name')
    
    if file_name:
        return open_file_helper(file_name)
    else:
        # If file_name is not provided.
        return {'error': 'file_name'}, 400
