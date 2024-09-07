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

    # The URL to be downloaded
    url = "https://www.youtube.com/watch?v=XFy6w6K5Ys0"
    # The path where the file needs to be downloaded
    filePath = "./videos"
    # File name to be downloaded
    fileName = "video1.mp4"
    # The file extension
    fileExtension = ".mp4"

    # Checking if the file exists or not
    if os.path.exists(os.path.join(filePath, fileName + fileExtension)):
        return "File already exists"
    else:
        # Downloading the file
        os.system("youtube-dl -f'mp4[height<=720