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

    data = request.data.decode('utf8')
    #check if a parameter was passed in URL
    if 'parameter' in data:
        #get parameters from request
        regex = request.args.get('regex')
        data = request.args.get('data')

    else:
        #get parameters from request
        regex = request.form['regex']
        data = request.form['data']

    #regex match function
    matchObj = re.search(regex, data)

    if matchObj: return "Match found"
    else: return "No match found"
