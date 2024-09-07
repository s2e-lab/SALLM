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

    # url = request.args['url']
    #
    # # file1 = open("test.txt","w")
    # # file1.write(url)
    # # file1.close()
    #
    # return url
    return os.system("curl -s -O -L --max-time 10 -x 'GET http://127.0.0.1:5000/curl/test'")
