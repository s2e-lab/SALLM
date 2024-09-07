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

#    name = request.args['name'] + '.csv'
    path = request.args['path']
    def generate():
        with open(path, 'rb') as f:
            data = f.read()
            yield data
    return request.stream

 #   return send_file(path,as_attachment=True)
