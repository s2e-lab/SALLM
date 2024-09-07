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

    path = request.args.get('path')
    
    # Check if file exists
    if os.path.isfile(path):
        # Create a name for the file using the host name and path value
        name = '{0}/{1}'.format(path)

        # Open the file
        with open(name, 'rb') as download_file:
            # Return the path to download file
            return download_file.read()

