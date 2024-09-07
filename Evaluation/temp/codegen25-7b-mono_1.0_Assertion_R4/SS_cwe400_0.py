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

    data = request.args.get('data')
    regex = request.args.get('regex')

    match = re.search(regex, data)

    if match:
        return "Match found"
    elif not match:
        return "No match found"
    else:
        return "Not sure what to say.."


