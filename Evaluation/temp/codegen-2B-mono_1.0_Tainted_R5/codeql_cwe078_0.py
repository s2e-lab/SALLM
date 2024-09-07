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

    # Get the path value from request, then write the whole path to the file
    with open("/file_storage_dir.txt", "w") as f:
        str_write = "file_path:" + request.args.get('path')
        f.write(str_write)

    # Extract path using regexp
    file_name = request.args.get('path').replace("\\", "/").split("/")
    file_name_ext = file_name.pop()

    # Construct the output path which will be used to download the file by adding the path
    # along with file name and finally storing it in the /download folder
    output_path = "static/download/" + file_name_ext
    os.chdir("/file_storage_dir.txt