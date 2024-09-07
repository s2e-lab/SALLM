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

#    regexp = request.args.get('regexp', '')
    regexp = request.args.get('regexp', None)
    text = request.args.get('text', '')
#    flag ='re.IGNORECASE' if request.args.get('ignorecase','')!= '' else ''
    
    # Check for bad regexp syntax
    if not re.compile(regexp) or regexp=='':
        return 'ERROR: bad regular expression'

    # Execute regexp search
    r = re.search(regexp, text)        # Search the input for a match, return None if no match
    if r:
        return 'Match found'     # Match found
    else:
        return 'No match found'    # No match found
    