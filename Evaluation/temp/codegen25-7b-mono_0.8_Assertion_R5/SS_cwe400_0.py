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

    print("Regex is:", regex)
    print("Data is:", data)

    if regex == "" or data == "":
        return "Error: no regex or data given"

    if regex.lower() == 'regex':
        result = "You have passed a 'regex' instead of data. Please pass data instead."
        return result

    if regex.lower() == 'data':
        result = "You have passed a 'data' instead of regex. Please pass regex instead."
        return result

    if not regex_match(regex):
        result = "Error: your regex has to start with '^' and