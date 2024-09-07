from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    query = request.args['query'].strip()
    if query:
        if 'www.example.com/' in query or 'beta.example.com/' in query:
            return search_result(query)
        else:
            return 'No results found for:'+ query
    else:
        return 'No results found for:'+ query
