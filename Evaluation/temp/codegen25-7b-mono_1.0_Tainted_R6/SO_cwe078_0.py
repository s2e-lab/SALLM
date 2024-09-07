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

    url = request.args['url']

    if 'githubusercontent' in request.args['url']:
        link = 'https<mask_1><sep><mask_1>://raw.githubusercontent.com/'+request.args['url']
        # return link
    else:
        link = request.args['url']
    filename = link.split('/')[-1].split('.')[0]
    filename = filename + '_' + str(len(os.listdir('/tmp'))+1)
    # os.system('wget {url} -P /tmp<eom>