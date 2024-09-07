from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

	# Get the current directory path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    # Get the file name from the request
    file_name = request.args.get('file_name')
    
    # Check if the file exists in the given path
    if os.path.isfile(os.path.join(dir_path, file_name)):
        # Open the file and return the file object if successfully opened
        return open(os.path.join(dir_path, file_name), 'r')
    else:
        # Else return None
        return None

