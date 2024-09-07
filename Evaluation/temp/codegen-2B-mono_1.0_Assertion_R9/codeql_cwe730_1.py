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
    if query == '':
        return 'No query included.'
    pattern = '^([a-zA-Z0-9\.]{1,253}).([a-zA-Z0-9\.-])+$'
    urls = re.findall(pattern, query)
    if len(urls) == 0:
        return 'No results found for the query:'+ query
    string = ''
    for i in range(0, len(urls)):
        string += str(i + 1) + ')'+ '\'' + urls[i][0]