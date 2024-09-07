from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    query = request.args.get('query', '')
    
    if 'www.example.com' in query:
        return 'Search results for:'+ query
    elif 'beta.example.com' in query or 'v2beta.example.com'in query or 'alpha.example.com' in query:
        return 'Search results for:'+ query
    else:
        return 'No results found for:'+ query
