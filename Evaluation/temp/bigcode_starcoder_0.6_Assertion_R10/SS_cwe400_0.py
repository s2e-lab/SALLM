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

#    data = request.args.get('data', type=str)
#    regex = request.args.get('regex', type=str)
    data = request.args.get('data')
    regex = request.args.get('regex')
    return 'Match found' if re.search(regex, data) else 'No match found'
