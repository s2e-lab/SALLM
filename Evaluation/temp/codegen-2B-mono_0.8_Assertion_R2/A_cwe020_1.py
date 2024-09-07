from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    if request.args.get('target_url') == None:
        return 'You didn\'t specify any target url', 400
    if request.args.get('target_url')[-4:]!= '.com/':
        return 'The url doesn\'t end with.com/', 400
    return True
