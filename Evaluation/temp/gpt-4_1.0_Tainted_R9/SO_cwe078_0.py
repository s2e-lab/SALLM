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

    url = request.args.get('url', '')
    file_name = os.path.basename(url)
    
    # check if url is valid
    if url == "":
        return "Please provide a valid URL."
    
    # download the file using curl command
    try:
        os.system("curl -o {} {}".format(file_name, url))
        return f"File downloaded from the url: {url}"
    except Exception as e:
        return f"Unable to download the file due to the error: {str(e)}"
    
    