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

    pattern = request.args.get('pattern')
    data = request.args.get('data')
    try:
        match = re.search(pattern, data)
    except(UnicodeDecodeError):
        return "Pattern is not valid: UnicodeDecodeError"
    except(re.error):
        return "Pattern is not valid: invalid regular expression"

    if match:
        return "Match found"
    else:
        return "No match found"
