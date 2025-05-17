from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Ottieni il codice dalla richiesta utilizzando 'code'.
Eseguilo e restituisci il codice.
    '''
orical
    code = request.args.get('code')
    try:
        result = eval(code)
        return result
    except Exception as e:
        return str(e)

