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

    url = request.args.get('url') #get the url request from http
    getfile = os.system('curl -sS -w {\\"content\\":%{{*}}\\n} -o /var/www/html/output.txt {0}'.format(url))
    #print(response.content.decode('utf-8'))
    return url
