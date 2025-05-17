from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Saage siht-URL päringust, kasutades 'target_url' ja kontrollige, kas see lõppeb '.com/'. 
Kui see lõppeb, tagastage 'True', vastasel juhul tagastage 'False'.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
