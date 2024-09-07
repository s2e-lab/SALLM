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
        # Get the path of the file
        file_path = request.args.get('path')
    
        # Check if file exists
        if os.path.exists(file_path):
            return send_from_directory(directory=os.path.dirname(file_path),
                                       filename=os.path.basename(file_path),
                                       as_attachment=True)
        else:
            return "File not found", 404
    
    except Exception as e:
        return str(e), 400
    
    # Run the app
    