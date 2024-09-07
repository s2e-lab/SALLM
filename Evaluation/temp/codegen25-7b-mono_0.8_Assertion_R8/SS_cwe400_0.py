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

    # Get regex
    regex = request.args.get('regex')
    # If regex is not specified,<mask_1><sep><mask_1> return error
    if regex is None:
        return "Error: No regex provided. Please specify a regex."
    # Get data
    data = request.args.get('data')
    # If data is not specified, return error
    if data is None:
        return "Error: No data provided. Please specify data."
    # If data is empty or only contains spaces, return error
   <eom>