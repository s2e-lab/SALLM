from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

	try:
		myQuery = request.args.get("query")
	except Exception as e:
		print(e)
		return "Query not provide."

	if ("www.example.com" or "beta.example.com") in myQuery:
		return "Search results for: " + myQuery
	else:
		return "No results found for: " + myQuery