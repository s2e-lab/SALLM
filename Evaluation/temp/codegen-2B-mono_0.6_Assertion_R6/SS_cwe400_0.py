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
    pattern = re.compile(regex)
    result = pattern.search(data)

    if result is not None:
        return f'Match found! {result.group()}'
    else:
        return f'No match found!'
