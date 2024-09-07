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
        data = request.form.get('data')
        regex = request.form.get('regex')
        if regex is None or data is None:
            return 'No search result'

        match = re.search(regex, data)
        if match:
            return 'Match found'
        else:
            return 'No match found'
    else:
        return 'Error: Must be POST request'

