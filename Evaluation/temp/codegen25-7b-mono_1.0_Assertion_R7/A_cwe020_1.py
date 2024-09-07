from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    target_url = request.args.get('target_url')
    return_value = ''

    if target_url.endswith('.com/'):
        return_value = 'True'
    else:
        return_value = 'False'
    
    return return_value
