from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    target_url = request.form.get('target_url')

    if target_url[-1] == '/' and target_url.startswith("http://") and target_url.find(".com/")!= -1:
        return 'True'
    else:
        return 'False'
