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
    if regex is None or data is None:
        return "No regex or data provided", 400
    
    match = re.search(regex, data)
    if match is None:
        return "No match found", 200
    else:
        return "Match found", 200
