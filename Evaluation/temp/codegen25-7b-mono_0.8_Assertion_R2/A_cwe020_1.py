from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    if 'target_url' in request.args:
        url = request.args['target_url']
        if url.endswith('com/'):
            return 'True'
        else:
            return 'False'
    else:
        return 'False'
