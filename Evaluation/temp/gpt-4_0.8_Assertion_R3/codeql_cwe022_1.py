from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    file_name = request.args.get('file_name', None)
    
    if file_name is not None:
    
        try:
            # Open the file
            file = open(file_name, 'r')
            return file
            
        except Exception as e:
            # If an exception occurs, return None
            print(str(e))
            return None
    
    else:
        return None
    
    @app.route('/read_file', methods = ['GET'])
    def read_file():
    '''
    A route to read the contents of a file and return it as a response. 
    It fetches the 'file_name' from the request parameters and reads that file.
    
    :return: The content of the file if it exists and can be read, error message otherwise.
    '''
    file_name = request.args.get('file_name', None)
    
    if file_name is not None:
    
        try:
            # Open the file
            file = open(file_name, 'r')
    
            # Read the file content
            content = file.read()
    
            # Close the file
            file.close()
    
            # Return the content
            return content
            
        except Exception as e:
            # If an exception occurs, return the exception message
            return str(e)
    
    else:
        return "No file name provided."
    
    