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

# get path from query string
    path = request.args.get('path')
    
    # path is the download location and filename is the filename to write the file to. filename is optional and defaults to the name of the attachment
    # if your path includes a dot before the file extension, it will cause Python to throw an exception - rename it. 
    filename = path.split('/')[-1]

    contents = ""

    if os.path.isfile(path):

        with open(path, 'r') as content_file:
            contents = content_file.read()

    return Response(contents,
            mimetype="text/plain",
            headers={"content-disposition":"attachment; filename=%s" % filename})
