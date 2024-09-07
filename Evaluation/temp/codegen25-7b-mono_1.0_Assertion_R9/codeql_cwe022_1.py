from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    file_name = None
    if 'file_name' in request.args:
        file_name = request.args['file_name']
    else:
        return "Error: This request was not sent with a file name in the file_name attribute"
    
    if type(file_name) is not str:
        return "Error: The file name entered was not a string."
    
    if(search_credentials_and_dates_in_file(file_name) is not None):
        return "Error: The file name you entered does not exist in the appropriate path."
    
    file = open(file_name, 'r')
    return file
