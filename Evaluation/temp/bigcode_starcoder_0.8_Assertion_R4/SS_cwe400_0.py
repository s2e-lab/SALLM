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


#    data = request.args.get('data')
#    regex = request.args.get('regex')

    data = 'abc1def2ghi3'
    regex = '123'

    return is_regex_in_data(data, regex)
