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

	# Get regular expression and text from request
	re_text = request.args('re')
	text = request.args('text')
	match = re.search(re_text, text)
	if not match:
	    return("No match found!")
	return("Match found!")
