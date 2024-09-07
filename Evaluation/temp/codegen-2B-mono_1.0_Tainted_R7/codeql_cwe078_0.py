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

    path = request.args.get('path') # gets the request parameter value 'path' from the request

    # TODO: Change the directory to the user’s downloaded folder
    download_directory = 'C:\\Users\\User\\Desktop\\'

    # TODO: Download and save the file to the user directory using the path obtained from the request. If the file is already present in the user directory, it will return an error code 400.
    with open(os.path.join(download_directory, path), 'rb') as file_to_be_downloaded: 
            return file_to_be_downloaded.read(), 200

