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

    data = request.get_json()
    regex = data['regex']
    data = data['data']
    result = ''
    for line in data:
        if re.search(regex, line):
            result += "Match found\n"
        else:
            result += "No match found\n"
    return result
