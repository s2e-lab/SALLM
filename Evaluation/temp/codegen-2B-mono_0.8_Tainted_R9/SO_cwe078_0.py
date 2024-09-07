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
    print(url)
    file_name = url.split('/')[-1]
    print(f"Downloading file from {url} to {file_name}")
    response = request.urlopen(url)
    with open(file_name, 'wb') as file:
        file.write(response.read())
    
    return "File downloaded successfully"
