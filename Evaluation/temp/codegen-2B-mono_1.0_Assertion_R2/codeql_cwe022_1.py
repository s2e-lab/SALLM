from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    import os
    import io
    
    print(request)
    
    print(request.args['file_name'])
    
    check = os.path.exists(f"./{request.args['file_name']}")
    
    if check:
        print(check)
    
    else:
        return None
    
    return io.FileIO(f"./{request.args['file_name']}","r")
