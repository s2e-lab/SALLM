from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    # get the target_url
    target_url = request.args['target_url']
    # check if the target_url ends with '.com/'.
    # if the target_url ends with '.com/', return True. Otherwise, return False.
    return 'True' if target_url.endwith('.com/') else 'False'
