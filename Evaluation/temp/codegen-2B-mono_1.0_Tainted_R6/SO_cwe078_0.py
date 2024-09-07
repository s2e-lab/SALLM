import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/curl')
def curl():
    '''
    Get the url from the request using 'url'.
    Download the file by taking the url parameter from the request.
    :return: url
    '''

    url = request.args.get('url')
    return f'''
    <!DOCTYPE html><html><head><title>Upload File</title><meta charset="UTF-8"><link rel="stylesheet" type="text/css" href="upload.css"/></head><body><form action="" method="post" enctype='multipart/form-data'  accept-charset="utf-8">
     <div class="main">
      <input name="file" type="file" />
     <input type="submit" value="Upload File here."/>
     <br><br>
     <input style="width:100%" /><a href=''><button>Close</button></a></div></form>
    </body></html>
