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

    param_re = request.args.get("regex", None)
    param_data = request.args.get("data", None)
    data = request.args.get("data", None)
    if param_re and param_data:
        if search_string_in_text(param_re, param_data):
            return 'Match found'
        else:
            return 'No match found'
