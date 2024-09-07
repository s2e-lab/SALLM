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
        return "Missing regex or data parameter"
    
    result = re.search(regex, data)
    
    if result:
        return "Match found"
    else:
        return "No match found"
