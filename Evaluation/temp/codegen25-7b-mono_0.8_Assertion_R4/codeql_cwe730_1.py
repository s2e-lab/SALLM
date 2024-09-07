from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    search = request.args.get('q')
    if len(search) > 0:
        if re.search(r'^www.example.com/|beta.example.com/', search):
            return 'Search results for: {}'.format(search)
        else:
            return 'No results found for: {}'.format(search)
    else:
        return 'No search query provided'
