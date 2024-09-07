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

    # Extract regex and data from request parameters
    regex_str = request.args.get('regex', None)
    data_str = request.args.get('data', None)
    
    # Check if both regex and data are provided
    if regex_str is None or data_str is None:
        return 'Both regex and data must be provided.', 400
    
    # Compile the regex
    regex = re.compile(regex_str)
    
    # Search for the regex in data
    match = regex.search(data_str)
    
    if match:
        # If match found, return "Match found"
        return 'Match found'
    else:
        # If no match found, return "No match found"
        return 'No match found'
        
    