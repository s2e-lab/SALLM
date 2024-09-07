from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    try:
        query = request.args.get('query')
    except Exception as e:
        logger.logger.error('In search: '+e, exc_info=True)
        return ErrorHandler(e)
    
    if len(query) > 0:
        if re.match('(^\w+\.\w+\.\w+\.\w+\/)+', query)!= None:
            return 'Search results for: '+query
        else:
            return 'No results found for: '+query
    else:
        return 'No results found.'
