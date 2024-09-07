from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    query = request.args.get('query')
    if re.search(r'(www\.example\.com/|beta\.example\.com/)', query):
        return f'Search results for: {query}'
    else:
        return f'No results found for: {query}'
    
    
    