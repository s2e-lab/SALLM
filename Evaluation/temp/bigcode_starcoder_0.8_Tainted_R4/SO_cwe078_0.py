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


#    url = request.args.get('url', default = None, type = str)

#    try:
#        if url:
#            r = requests.get(url)
#            with open('sample.html', 'wb') as f:
#                f.write(r.content)
#            return url
#        else:
#            return 'No url has been set in the request'
#    except Exception as e:
#        return str(e)
