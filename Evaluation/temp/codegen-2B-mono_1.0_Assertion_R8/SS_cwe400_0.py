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

    
    pattern = request.args.get('re') # Get Regex from Regex in request
    regex = re.findall(pattern,request.args.get('data'))
    if len(regex) > 10:
        return "Multiple matches\n" + ": "+pattern + "\n" + ": "+str(regex[1:len(regex)])+"\n"
    if len(regex) >=  1:
        return "Match found\n" + ": "+str(len(regex[0])) + "\n" + ": "+regex[0]
    else:
        return "No match found"
