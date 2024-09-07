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

# The URL of the file to download with the url in the request.
    url = request.args.get('url', '')

    # Download the file from the URL.
    # Specify the path to save the file to, also known as the "download" path.
    with open(os.path.join(app.root_path, 'downloads', 'video.mp4'), 'wb') as file:
        response = requests.get(url)
        file.write(response.content)

    return url
