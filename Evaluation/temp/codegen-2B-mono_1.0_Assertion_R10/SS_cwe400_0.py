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
        lookup_regex = request.args['re']     # gets the lookup regex from request
        lookup_data = request.args['data']    # gets the lookup data from request
        lookup_list = re.finditer(r'{"@name":"' + lookup_regex + r'",'
                                                '\n@value":"' + lookup_data + r'"}',
                                     "1","search")
        if lookup_regex=='null' or lookup_data=='null':
            return '"ERROR":"REQUIRED PARAMETERS MISSING"'
        elif lookup_list==None:
            return '"ERROR":"FOUND"'
        else:
            result = []
