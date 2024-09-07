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

    data = request.args.get('data')
    regex = request.args.get('regex')
    
    if(regex == None or data == None):
        return("400 Bad Request")
    elif(regex == "" or data == ""):
        return("400 Bad Request")
    else:
        if re.search(regex, data):
            return("Match found")
        else:
            return("No match found")

