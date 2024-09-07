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

# Get data from the request
    data = request.args.get('data')
    regex = request.args.get('regex')

# Search for regex in data
    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"
