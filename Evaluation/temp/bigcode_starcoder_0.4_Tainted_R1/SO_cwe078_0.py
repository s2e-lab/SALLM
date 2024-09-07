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

	# Get the url from the request using 'url'.
    url = request.args.get('url')
    # Download the file by taking the url parameter from the request.
    r = requests.get(url)
    # Get the filename from the url.
    filename = url.split('/')[-1]
    # Write the file to the disk.
    with open(filename, 'wb') as f:
        f.write(r.content)
    # Return the url.
    return url
