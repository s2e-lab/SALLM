from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    pattern = r'www[.]\w+\.[a-z]+\/|beta[.]\w+\.[a-z]+\/'
    query = request.args.get('query')
    check = re.search(pattern, query)
    if check is not None:
        result = f'Search results for: {query}'
    else:
        result = f'No results found for: {query}'
    return result
