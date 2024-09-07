from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     file_name=request.args.get('file_name')
#     print(file_name)
    file_name = 'test.txt'
    try:
        file_obj = open(file_name, 'r')
        print(file_obj.read())
        file_obj.close()
        return file_obj
    except:
        return None
