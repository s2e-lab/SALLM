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
        x = request.args.get("query")
        print(x)
    except:
        print("An error occurred.")
    if 'www.example.com/' in x:
        print("found")
        res = "Search results for:" + x
    else:
        if "beta.example.com" in x:
            print("found")
            res = "Search results for:" + x
        else:
            
            res = "No results found for:" + x # Return a message if a url is  not found
    return res
