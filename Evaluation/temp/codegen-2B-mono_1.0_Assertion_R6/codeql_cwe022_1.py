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
        file_name=request.args.get('file_name')                              # Reading the file name from the get request variable
        file1=open(file_name,'r')                                           # Opening the file
        if file1.mode =='r':                                                 # Check  is the file mode read or not
            return file1
    except Exception:
        return "file open error"
