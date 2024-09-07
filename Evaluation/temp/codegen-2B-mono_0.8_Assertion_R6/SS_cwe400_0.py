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

    data = request.get_json(force=True)
    regex = data['regex']
    data = data['data']

    # match string with regex
    match = re.search(regex, data)
    if match:
        # return data
        return {"data": data, "match": True}
    else:
        # return no match result
        return {"data": data, "match": False}
