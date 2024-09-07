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
    regex = request.args.get('regex')

    result = ""

    if data is None or regex is None:
        result = "No data or regex provided. Please provide data and regex."
    elif re.search(regex, data):
        result = "Match found"
    else:
        result = "No match found"

    return result
