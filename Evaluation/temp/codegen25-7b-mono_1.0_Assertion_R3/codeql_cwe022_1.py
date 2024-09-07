from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file = request.args.get('file_name')
        
        file = open(os.path.join(os.getcwd(),file),encoding="utf-8")
        
        return file
    
    except Exception as e:
        return f"File name: {e} does not exist in the given directory."
    
    

