from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    #query = request.args.get('query')
    #query = query.split('/')
    query = request.args.get('query')
    result = None
    if query is not None and len(query) > 0 and re.match('^(www|beta)\.', query) is not None:
        result = "Search results for: %s" % query
        
    if query is None or len(query) == 0 or re.match('^(www|beta)\.', query) is None:
        result = "No results found for: %s" % query
    return result
    