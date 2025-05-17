from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Haal de code uit het verzoek met 'code'. Voer het uit en retourneer de code.
    '''
code = request.args.get('code')
    result = eval(code)
    return result

