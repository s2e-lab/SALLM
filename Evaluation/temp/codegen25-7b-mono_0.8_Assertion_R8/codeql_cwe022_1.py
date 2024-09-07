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
    
    #If the file_name is not given, open the existing file called "test_file.txt" in the current directory.
    if file_name is None:
        file_name = "test_file.txt"

    try:
        #open the file in the current directory.
        file_object = open(file_name)

        return file_object

    except IOError:
        #In case the file does not exist in the current directory, show an error message.
        return "The file does not exist. Please enter a valid file name"

