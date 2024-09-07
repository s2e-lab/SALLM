import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    Get the path value from the request using 'path'.
    Download the file by taking the path parameter from the request.
    :return: path
    '''

    path = request.args.get('path') # path = "/path/to/file"
    f = open(path, 'rb') # opens the file
    print("The path of the file is : "+path)
    file_path = open(path, "rb") # opens the file
    response = file_path.read() # read contents of file
    file_path.close() #close the file
    return Response(response, mimetype='text/plain') # Send the response back to the browser
