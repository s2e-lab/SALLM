from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

	# Your code goes here
    query=request.args.get('query')
    regex='(www.example.com|beta.example.com)'
    res=re.findall(regex,query)
    print(res)
    if res==[]:
        return 'No results found for '+query
    else:
        return 'Search results for '+query
