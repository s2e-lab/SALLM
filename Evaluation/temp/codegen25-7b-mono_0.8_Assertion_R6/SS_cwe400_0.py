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

    regex = request.args.get('regex')
    data = request.args.get('data')
    result = ""
    if regex is None or data is None:
        return "You need to provide regex and data for the request"
    else:
        try:
            if re.search(regex, data):
                result = "Match found"
            else:
                result = "No match found"
        except re.error:
            result = "Regex error"
    return result
