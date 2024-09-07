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
    search_data = request.args.get('data')
    
    # make sure everything is sanitised
    try:
        if re.match("[0-9]+", regex) or re.match("[0-9]+[^[A-Za-z]+", regex) or re.match(regex, "\\n") or re.match("[0-9]+[^\r]+", regex) or "\\" in regex:
            return "Regular expression is malformed. Please check it then try again"
        elif (re.search("[a-zA-z]", search_data) is None) and re.search(r"\r[\