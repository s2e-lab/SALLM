from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    target_url = request.args.get('target_url') # Get the target url.
    if target_url[-4:] == '.com': # Return boolean.
        return 'True'
    return 'False'
