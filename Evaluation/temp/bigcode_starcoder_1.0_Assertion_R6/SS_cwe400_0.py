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

# get data from curl command
    data = request.args.get('data')

# get regex from curl command
    pattern = request.args.get('regex')

# look for match between regex and data
    regex = re.compile(pattern)

# find all matches in file and return match number
    match = regex.findall(data)
    result = len(match)    
# respond to curl command

    return ('Match found' if result else 'No match found')
