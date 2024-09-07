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
        regex = request.args.get("regex").strip()
        data = request.args.get("data").strip()
        result = False

        if regex and data:
            # find regular expression
            find_match = re.findall(regex, data)
            # add found string in case of there is multiple matches
            # example: "abc  def" --> "abc", "bc"
            #   and not "abc, def" because that is already the answer
            find_all = ",".join(find_match)

            # find matched data in data
            find_matched = re.findall(rf'\b{find_match}\b', data)
            find_all +='and '