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

    data = request.args.get('data')
    if data is None:
        return "data not found"
    regex = request.args.get('regex')
    if regex is None:
        return "regex not found"
    if re.search(regex, data):
        return "Match found"
    return "No match found"
