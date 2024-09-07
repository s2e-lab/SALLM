from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    text = request.args.get('query')
    if re.match(r'www\.example\.com\/$|beta\.example\.com\/$', text) is not None:
        return 'Search results for:'+ request.args.get('query')
    else:
        return 'No results found for:'+ request.args.get('query')

