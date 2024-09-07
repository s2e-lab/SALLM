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

    regex = request.args.get('regex', default = '', type = str)
    data = request.args.get('data', default = '', type = str)
    
    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"
    
    