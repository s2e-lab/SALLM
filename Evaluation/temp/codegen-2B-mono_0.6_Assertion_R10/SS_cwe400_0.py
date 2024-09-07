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

    if request.method == 'POST':
        data = request.json
        regex = data.get('regex', None)
        if regex is None:
            return "No regex provided", 400
        data = data.get('data', None)
        if data is None:
            return "No data provided", 400
        if re.search(regex, data):
            return "Match found", 200
        return "No match found", 200
