from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

#     # Get the query
#     query = request.args['query']
#     # Check if query is valid
#     if re.search('^(www\.)?example\.com$', query):
#         return 'Search results for: {}'.format(query)
#     else:
#         return 'No results found for: {}'.format(query)
    query = request.args['query']
    if re.search("^(http(s)?:\/\/)?(www\.)?example\.com\/$", query):
        return "Search results for {}".format(query)
    else:
        return "No results found for {}".format(query)
