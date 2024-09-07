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

    regex = request.args.get("regex")
    data = request.args.get("data")
    # find() - will match a single instance of regex in data
    if data:
        print(data)
        if regex and data:
            matcher = re.compile(regex)
            print("matches: ", matcher.findall(data))
            return {'result': 'match found'}
        else:
            return {'match': 'No match found'}
    else:
        return {'failure': 'missing data'}

