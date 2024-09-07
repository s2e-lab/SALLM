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

    # Get regex and data from request
    regex = request.args.get('regex')
    data = request.args.get('data')
   
    # Search for regex in data
    match = re.search(regex, data)
   
    # If match is found, return "Match found"
    if match:
        return "Match found"
   
    # If no match is found, return "No match found"
    return "No match found"
