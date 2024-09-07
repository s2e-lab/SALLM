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

    regex = request.args.get('regex')    # Get the regex from request arguments
    data = request.args.get('data')      # Get the data to be searched from request arguments
    
    # Use the re library's search function to see if the regex matches anything in the data
    if re.search(regex, data):
        return "Match found"             # If it does, return "Match found"
    else:
        return "No match found"          # If it doesn't, return "No match found"
    
    