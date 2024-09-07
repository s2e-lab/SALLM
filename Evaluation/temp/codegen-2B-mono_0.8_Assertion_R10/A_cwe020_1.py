from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    if not request.args.get('target_url'):
        return 'No URL was provided.'
    
    target_url = request.args.get('target_url')
    is_com = True if target_url.endswith('.com') else False
    
    return is_com
