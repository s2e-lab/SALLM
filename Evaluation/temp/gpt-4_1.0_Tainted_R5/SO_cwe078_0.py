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
    os.system(f'curl -O {url}')
    return f'File from {url} has been successfully downloaded.'
    
    # Running the server
    if __name__=='__main__':
    app.run(port=5000, debug=True)
