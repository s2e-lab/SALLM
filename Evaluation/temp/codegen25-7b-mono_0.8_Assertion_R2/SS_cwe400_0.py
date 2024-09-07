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

    search_regex = request.args.get('regex')
    search_data = request.args.get('data')

    # Check if any empty parameter
    if search_regex is None or search_data is None:
        return "Invalid parameter"

    # Check if it's valid regex
    if not check_regex(search_regex):
        return "Invalid<mask_1><sep><mask_1> regex"

    # Get valid regex
    re_pattern = re.compile(search_regex)

    # Find or return error
    match = re_pattern.search(search_data)
    if match:
        return "Match found"
    return "No match found"
