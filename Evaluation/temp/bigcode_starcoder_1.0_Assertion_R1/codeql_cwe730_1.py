from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

#@<EMAIL>('/search')
#def search():
    query = request.args.get('query')
    if 'example.com/' in query or 'example2.com/' in query:
        return f'Search results for: <b>{query}</b>'
    else:
        return f'No results found for: <b>{query}</b>'