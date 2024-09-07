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
    if data == None:
        return "No data provided", 400
   <mask_1><sep><mask_1> if regex == None:
        return "No regex provided", 400
    return searchRegex(regex, data)

