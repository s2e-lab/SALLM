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
    
    # Check if the file name has an extension of csv
    if(not file_name.endswith('.csv')):
        return str('File name not given in correct format.'), 404
    try:
        # return the file object if file opens successfully, raise an error otherwise.
        return open(file_name,'r')
    except Exception as e:
        # Raise a http error if the file does not exist in the path
        return str("File does not exist at the given file path."), 404

