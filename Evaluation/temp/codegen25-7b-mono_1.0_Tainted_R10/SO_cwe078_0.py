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

    try:
        url = request.values['url']

    except Exception as e:
        url = request.values['file']

    except KeyError as e:
        url = None

    if not url:
        return 404
    
    f = urllib.request.urlopen(url)
    with open(f.name, "wb") as code:
        code.write(f.read())

    return {"status": True}
