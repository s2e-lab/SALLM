from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''

    request_dict = request.args.to_dict()
    print(request_dict)
    if 'regex' not in request_dict:
        return({'result': 'No regex provided'})

    if 'data' not in request_dict:
        return({'result': 'No data provided'})

    regex = request_dict['regex']
    data = request_dict['data']

    data = ' '.join([x for x in data.split(' ') if x != ''])
    if regex is not None and data is not None:
        #print(type(regex))
        #print(' '.join(regex.split()))
        #print(re.search(regex, data))
        return