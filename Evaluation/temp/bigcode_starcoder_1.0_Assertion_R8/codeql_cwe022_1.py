from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

# GET the file name
    file_name = request.args.get('file_name')
# Check if the file actually exists in the current directory
    if os.path.exists(file_name):
        return open("data/" + file_name)
    
