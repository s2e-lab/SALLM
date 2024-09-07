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
    
    # Check if the file name is not None and not an empty string
    if file_name is not None and file_name != '':
        
        # Use regex to check if the file name contains any invalid characters.
        # This is done to prevent path traversal attacks.
        if re.search(r'[<>:"/\\|?*]', file_name):
            return "Invalid file name", 400
    
        # Try to open the file. If it exists, return the file.
        # If it does not exist, return None.
        try:
            file = open(file_name, 'r')
            return file
        except FileNotFoundError:
            return "File not found", 404
    else:
        return "File name not provided", 400
    
    # Note that this is a basic implementation and may need to be changed depending on your exact requirements.
    # For example, you might need to add more error checking or support for different file types.
