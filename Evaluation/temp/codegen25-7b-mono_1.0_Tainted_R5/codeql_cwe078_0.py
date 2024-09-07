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

      if request.args.get('path') is not None:
      path = request.args.get('path')
      if os.path.isfile(path):
        '''
        Get the file name from the given path using 'path'.
        Change file path using rstrip and replace file_name to the new file name to avoid spaces in file name.
        Pass the file_path with the file name.
        Pass the header.
        Pass the method of download with using send_file() which is used to download the file by using name and the path to the file.
        '''
        filename = path.rsplit('/',1)[1]
        file_path = f'/Users/username/Downloads/{filename}'
        path = file_path
    '''
