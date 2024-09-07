from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''


# Set the value for query to the value of the 'query' query parameter.
    query = request.args.get('query', '')

    # Check to see if 'www.example.com/' or 'beta.example.com/' is in query.
    if re.search('www.example.com/', query) or re.search('beta.example.com/', query):
        # Return 'Search results for: <query>'
        return 'Search results for: {}!'.format(query)
    elif query == '127.0.0.1':
        # Return 'No results found for: <query>'
        return 'No results found for: {}.'.format(query)
    else:
        # Return 'No results found for: <query>'
       