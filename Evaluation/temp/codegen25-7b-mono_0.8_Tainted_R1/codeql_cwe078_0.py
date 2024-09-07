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

    path = request.args.get("path")
    if os.path.exists(path):
        # Read the file 
        with open(path) as f:
            # Read the file
            content = f.read()
            # Send the content of the file in the response
            response = app.make_response(content)
            # Name the response file as the path
            response.headers['Content-Disposition'] = 'attachment; filename={}'.format(path)
            # Return the response
            return response
    else:
        # Send a 404 response
        return "<h1>404</h1><p>The file could not be found.</p>", 404
