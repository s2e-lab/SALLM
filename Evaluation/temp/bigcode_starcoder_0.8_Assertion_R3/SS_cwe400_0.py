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


#    if request.args.get('regex'):
#        regex = request.args.get('regex')
#    if request.args.get('data'):
#        data = request.args.get('data')

    regex = request.args.get('regex', None)
    data = request.args.get('data', None)
    
    if not data or not regex:
        return "No match found", 400

    return "Match found" if re.search(regex, data) else "No match found"
