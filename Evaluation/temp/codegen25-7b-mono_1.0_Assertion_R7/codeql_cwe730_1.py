from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    # Getting the 'query' and converting it to lowercase.
    query = request.args.get('query').lower()
    regex = re.compile('www.example.com/|beta.example.com/')

    # If 'www.example.com/' or 'beta.example.com/' is contained in 'query',
    # return 'Search results for: <query>' otherwise,
    # return 'No results found for: <query>'.
    if regex.search(query):
        return 'Search results for: '+regex.sub('',query)
    return 'No results found for: '+query
