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

    download_url=request.args.get("url")

    # Get the file from the server
    file=requests.get(download_url,stream=True)
    filename=download_url.split('/')[-1]
    dst = os.path.abspath(os.path.join('/tmp', filename))
    with open (os.path.join(dst),'wb') as f:
        for chunk in file.iter_content(chunk_size =1024*1024):
            if chunk:
                f.write(chunk)
    
from bs4 import BeautifulSoup 
import requests
import os
from flask import Flask, request, render_template

app2 = Flask(__name__)
