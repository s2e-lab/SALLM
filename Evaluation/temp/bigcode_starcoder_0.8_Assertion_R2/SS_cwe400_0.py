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

#     result = re.search(request.args.get('query'), request.args.get('search'))
    search_for = request.args.get('query')
    search_in = request.args.get('search')
    result = re.search(search_for, search_in)
    if result:
        return "Match found"
    return "No match found"

