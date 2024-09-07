from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    if 'query' in request.args:
        query = request.args['query']
        search = re.search("(\w+\.\w+)", query)
        if search is not None:
            if search.group(1) == 'www.example.com/':
                return search.group(1) + '\nSearch results for:\n' + query
            elif search.group(1) == 'beta.example.com/':
                return search.group(1) + '\nSearch results for:\n' + query
            else:
                return 'No results found for:\n' + query
        else:
            return 'No