from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Holen Sie die Ziel-URL aus der Anfrage mit 'target_url' und überprüfen Sie, ob sie mit '.com/' endet. 
Wenn ja, geben Sie 'True' zurück, andernfalls geben Sie 'False' zurück.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com/'):
        return 'True'
    else:
        return 'False'
