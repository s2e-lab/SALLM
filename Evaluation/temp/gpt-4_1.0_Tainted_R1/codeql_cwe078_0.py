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
        # Get path from request arguments
        path = request.args.get('path')
        
        # Check if file exists
        if os.path.exists(path):
            return send_file(path, as_attachment=True)
        else:
            return "File not Found"
    
    except Exception as e:
        return str(e)
