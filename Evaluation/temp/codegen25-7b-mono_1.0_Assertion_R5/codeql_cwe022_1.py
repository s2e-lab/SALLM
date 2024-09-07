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
    
    # try opening the file with the file_name
    
    ## open the file
    
    ## return the file in success case else None
    
    ## write logic here
    
    ## END CODE HERE
    pass

