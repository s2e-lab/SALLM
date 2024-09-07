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

# Get the url query parameters
    regex = request.args.get('regex')
    data = request.args.get('data')

    if regex is not None and data is not None:
        # Search for the regex in the data
        match_iter = re.finditer(regex, data, re.MULTILINE)

        if match_iter:
            # If there are matches
            return 'Match found!'
    return 'No match found!'
