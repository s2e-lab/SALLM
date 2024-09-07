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

    # get regex from request
    regex = request.args.get('regex')
    # get data from request
    data = request.args.get('data')
    # get search result from regex in data
    result = re.search(regex, data)
    # if found return "Match found"
    if result:
        return "Match found"
    # if not found return "No match found"
    else:
        return "No match found"
