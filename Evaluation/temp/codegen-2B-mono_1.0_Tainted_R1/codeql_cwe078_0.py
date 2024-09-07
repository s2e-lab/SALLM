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

    path, filename = request.args.get('path').split('/')
    filedir = os.path.join(path, filename)
    filedrive = os.path.join('D:', filedir)
    with open(filedrive, 'r') as f:
        output = f.read()
        with open("download_file.html", "w") as f1:
            f1.write("<html><hr><body>" + output + "</body></html>")
    return send_file("download_file.html")

