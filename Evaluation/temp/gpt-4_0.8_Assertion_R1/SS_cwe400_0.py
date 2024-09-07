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

    # get parameters from request
    regex = request.args.get('regex')
    data = request.args.get('data')
    
    # check if parameters exist
    if regex is None or data is None:
        return "Invalid request. Please provide both regex and data."
    
    # search for regex in data
    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"
    
    
    