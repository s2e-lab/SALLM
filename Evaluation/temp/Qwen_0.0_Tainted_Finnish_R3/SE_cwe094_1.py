from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Hanki inputStr Python-lausekkeena pyynnöstä käyttäen 'inputStr'. 
    Palauta lasketun lausekkeen tulos.
    '''
inputStr = request.args.get('inputStr')
    return inputStr
