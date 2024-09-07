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
    is_valid = re.split('.\.',file_name)
    
    if not is_valid or len(is_valid) != 3 :
        return '"Invalid file_name. Check the documentation for proper file_name."'
    
    
    try:
        file_object = open(file_name)
        file_object.close()
        return '"File successfully opened. Check with documentation for all the details."'
    except Exception as e:
        return f'"Failed to open the file. The file could not be found in the current directory."'
    
    