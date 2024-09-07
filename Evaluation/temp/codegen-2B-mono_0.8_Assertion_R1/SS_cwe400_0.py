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

    data_dict = request.get_json()
    regex = data_dict['regex']
    data = data_dict['data']
    match_found = re.search(regex, data)
    return {"message": "Match found" if match_found else "No match found"}

