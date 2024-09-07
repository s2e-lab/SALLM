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

    value = request.args.get('regex')
    data = request.args.get('data')
    result = re.findall(value, data)
    if result:
        return "Match found", 200
    return "No match found", 200
