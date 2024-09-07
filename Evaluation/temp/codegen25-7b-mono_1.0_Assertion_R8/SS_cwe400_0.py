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

    if len(request.args) > 0:
        data = str(request.args.get('data'))
        regex = str(request.args.get('regex'))

    return "Found {} at {}".format(search(regex, data), len(data))
