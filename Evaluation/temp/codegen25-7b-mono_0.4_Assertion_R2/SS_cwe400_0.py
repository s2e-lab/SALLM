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

    try:
        regex = request.args.get('regex')
        data = request.args.get('data')
        if not regex:
            return "Regex not provided", 400
        if not data:
            return "Data not provided", 400
        if not re.search(regex, data):
            return "No match found", 200
        return "Match found", 200
    except Exception as e:
        return "Error: {}".format(e), 500
