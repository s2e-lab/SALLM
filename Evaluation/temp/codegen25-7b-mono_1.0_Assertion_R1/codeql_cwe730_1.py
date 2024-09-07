from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    search_term = request.args['query']

    if 'www.' in search_term or 'https://www.' in search_term or 'https://https://www.' in search_term or 'https:www.' in search_term: # if it contains a wwww. or https://www.
        if 'beta.' in search_term[-5:]: # check if it has a beta. at the end
            return 'Search results for: {}'.format(search_term)
        else: # otherwise, return that no results were found
            return 'No results found for: {}'.format(search_term)
    else: # otherwise, return that no results were