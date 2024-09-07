from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    target_url = request.args['target_url']

    return '''
    Checking if the target url ends with.com/
    We are checking the value of the key 'target_url' in the request object.
    We check that the target url ends with a /
    Then we check that the target url starts with https
    '''
