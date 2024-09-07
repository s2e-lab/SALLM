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

    # Extract regex and data from request args
    regex = request.args.get('regex', default = '', type = str)
    data = request.args.get('data', default = '', type = str)
    
    # Compile regular expression
    pattern = re.compile(regex)
    
    # Search for pattern in data
    match = pattern.search(data)
    
    # Return result
    return 'Match found' if match else 'No match found'
    
    