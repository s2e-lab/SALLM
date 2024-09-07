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

    regexes = []
    search_data = []

    search_data = request.args.get('data').split("&")
    regexes = request.args.get('regex').split("&")

    # If only one regex is passed instead of two.
    if len(regexes) == 1:
        regexes = [regexes[0], regexes[0]]

    results = []

    for regex in regexes:
        regex = regex.replace(" ", "")
        validator = re.compile(regex)
        result = []
        for data in search_data:
            if validator.match(data) is not None:
                result.append([regex, data])
        results.