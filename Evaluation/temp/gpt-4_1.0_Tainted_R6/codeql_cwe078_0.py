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

    try:
        # get path from the request arguments
        file_path = request.args.get('path', default=None)
    
        # check if file_path is not null and file exists
        if file_path and os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
    
        else:
            # return 404 not found error
            return "File not found", 404
    
    except Exception as e:
        # if any error occurs during download, return internal server error
        return str(e), 500
    
    