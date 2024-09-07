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
    #regex = data["search_regex"]
    data = request.args.get('search_regex')
    print(data)
#    regex_list = json.loads(regex)
    data_file = open('sample_text.txt', 'r')
    reg = re.compile(data)
    data_file_content = data_file.read()
    match_result = reg.search(data_file_content)
    print(match_result)
    if match_result:
        return "Match found"
    #for row in data_file_content:
    #    for regex in regex_list:
    #        match = re.search(regex['regex'], row)
    #        if match:
    #            print(row)
    #            print(match.group