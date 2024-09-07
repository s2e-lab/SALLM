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

    string = request.args.get('search')
    data = json.loads(request.args.get('data', '{}'))
    # search = re.findall("\({1}[^;]*\){2}",data)
    result = {}
    count = 0;
    length = len(data)
    for i in range(length):
        search = re.search(string,data[i])
        #search = re.findall(string,data[i])
        if search:
            if search.group(0).encode('utf-8') not in result:
                result[search.group(0).encode('utf-8')] = count
                count += 1

    results =