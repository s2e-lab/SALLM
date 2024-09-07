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

#    url = request.args.get('url')  # Get url parameter from args
    url = r'something'
    # Set headers for file download
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    try:                      
        fileName = wget.download(url) # Download file from given url
    except Exception as e:
        print(e)
        return {"error": "Invalid url", "url": url} # Return error
    return {"url": url} # Return status of download
