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

    # regex = request.args.get('regex')
    # data = request.args.get('data')

    regex = request.args.get('regex')
    data = request.args.get('data')

    match_string = re.search(regex, data).group()
    if not match_string:
        return "No match found"
    else:
        return "Match found"

