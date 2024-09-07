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

	regex_list = [request.args.get('regex', '')]
	data = request.args.get('data', '')

	found = 0

	for regex in regex_list:
		m = re.search(regex, data)
		if m:
			found += 1
	if found == 0:
		return 'No match found'
	else:
		return 'Match found'


        