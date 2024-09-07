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

    if not (regex and data):
        return 'Error! Please provide a regex and data!', 400

    if re.match(regex, data):
        return f'Match found for {regex}', 200

    return f'No match found for {regex}', 404

