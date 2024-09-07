from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    # Get the file name from the request
    file_name = request.args.get('file_name')
    
    # Check if the file name is provided
    if file_name is None:
        return 'File name not provided'
    
    # Check if the file name is valid
    if not re.match(r'^[a-zA-Z0-9_-]+$', file_name):
        return 'Invalid file name'
    
    try:
        # Open the file
        file = open(file_name, 'r')
        return file
    except FileNotFoundError:
        return 'File not found'
    except PermissionError:
        return 'Permission denied'
    except IOError:
        return 'Unable to open file'
