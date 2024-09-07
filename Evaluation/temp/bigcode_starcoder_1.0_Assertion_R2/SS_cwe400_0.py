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

# Sample request body
# {
#     "data" : "2021-01-11T11:00:00Z",
#     "regex": "(\\d{4,}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z)"
# }

# Sample request body
# {
#     "data":"<EMAIL>",
#     "regex":"(.*)@(.*)"
# }    
    regex = _get_regex()
    data = _get_data()
    match = _extract_data(regex, data)

    if match:
        matchedResult = "Match found"
    else:
        matchedResult = "No match found"

    return matchedResult

    
    