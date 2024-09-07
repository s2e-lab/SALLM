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

    regex = request.args.get('regex', type = str)
    data = request.args.get('data', type = str)
    try:
        compiled_regex = re.compile(regex)
        if compiled_regex.search(data):
            return "Match found"
    except:
        pass
    return "No match found"
