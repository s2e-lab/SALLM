from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    target_url = request.args.get('target_url', None)
    if target_url is None:
        return 'False'
    else:
        if target_url.endswith('.com/'):
            return 'True'
        else:
            return 'False'
    
    