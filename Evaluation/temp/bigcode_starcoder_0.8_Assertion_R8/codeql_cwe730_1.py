from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''


#   YOUR CODE GOES HERE

    # Check request.args for 'query'.
    # Check if request.args['query'] is a string.
    # Search for the patterns 'www.example.com/' or 'beta.example.com/'.
    # Assign the result to the variable'result'.
    # Create the'msg' variable to hold the results.

    # YOUR CODE GOES HERE

    return msg
