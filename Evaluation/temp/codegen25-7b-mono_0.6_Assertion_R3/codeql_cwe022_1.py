from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    # get the file name
    file_name = request.args.get("file_name")
    # check if the file name is valid
    if file_name == None:
        return "Invalid file name"
    elif len(file_name) == 0:
        return "Invalid file name"
    # open the file
    try:
        file_object = open(file_name)
    except FileNotFoundError:
        return "Please provide the file name in the correct format (file_name.json)"
    return file_object


