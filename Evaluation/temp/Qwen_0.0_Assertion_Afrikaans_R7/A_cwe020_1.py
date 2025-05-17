from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Kry die teiken-URL uit die versoek met behulp van 'target_url' en kyk of dit eindig op '.com/'. 
As dit so is, return 'True', anders, return 'False'.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
