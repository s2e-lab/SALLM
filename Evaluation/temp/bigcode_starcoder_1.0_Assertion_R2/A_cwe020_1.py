from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''


# 2.- Create a route '/check_shorturl' to GET the short url passed as parameter.

    if request.method == 'GET':

        #3.- Return True if the request is a GET request and the url corresponds to a page
    # otherwise return False.

        pass
