from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

# Solution 1
    # query = request.args.get('query')
    # if re.search('www.example.com|beta.example.com', query):
    #     return 'Search results for:'+ query
    # return 'No results found for:'+ query

#Solution 2
    query = request.args.get('query')
    if re.search('www\.example\.com|beta\.example\.com', query):
        return 'Search results for: {0}'.format(query)
    return 'No results found for: {0}'.format(query)