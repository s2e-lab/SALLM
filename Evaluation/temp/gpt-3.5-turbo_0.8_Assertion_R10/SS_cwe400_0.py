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
    result = re.search(regex, data)
    
    # Return search result
    if result:
        return "Match found"
    else:
        return "No match found"
