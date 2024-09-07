from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    target_url = request.args.get('target_url')
    ends_with = False

    if target_url and not target_url.endswith('com'):
        ends_with = True

    return {
        'ends_with_com': ends_with,
        'target_url': target_url
    }
