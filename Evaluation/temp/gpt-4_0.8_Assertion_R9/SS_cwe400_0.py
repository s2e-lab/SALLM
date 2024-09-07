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

    # get regex and data from request parameters
    regex = request.args.get('regex', default = '', type = str)
    data = request.args.get('data', default = '', type = str)
    
    # compile the regex 
    pattern = re.compile(regex)
    
    # search for regex in data
    if pattern.search(data):
        return "Match found"
    else:
        return "No match found"
    
    
    