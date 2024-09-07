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

    #print(f"Data: \r\n{request.data}")
    data = request.get_json(force=True)  # json data

    # get data from request
    search_for = data.get("search", None)
    regex = data.get("regex", None)
    match = None

    if search_for and regex:
        # return "Error"
        print("Match found")

        try:
            # re searches for match in any expression
            match = re.search(regex, search_for).group(1)
        except Exception as e:
            print(e)
        else:
            # if no match, return 0 (no matches) instead
            #print(f"