from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    # Get the target url from the request
    target_url = request.args.get('target', '')
    # If the target_url is empty, return None
    if target_url == '':
        return None

    # Check if the target_url ends with '.com/'
    if target_url.endswith('.com'):
        # If true, return True
        return 'True'
    else:
        # If false, return False
        return 'False'
