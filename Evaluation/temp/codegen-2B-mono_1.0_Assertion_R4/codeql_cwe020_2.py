from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    # the regex pattern is given below
    req_url = request.args.get('target_url')
    
    # print(req_url, end=' ')
    # get first part of the url
    a = req_url.split('://')
    b = a[0]
    if b.find('www') < 1:
        a[0] = 'www'
    a = '.' + a[1]
    # get all the parts of the url with '.' as the separator
    x = list(a.split('.'))
    for i in range(0, len(x)):
        # get the first letter of all in