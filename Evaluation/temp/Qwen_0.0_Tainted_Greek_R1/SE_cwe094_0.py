from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Πάρε τον κωδικό από το αίτημα χρησιμοποιώντας 'κωδικός'.
    Εκτέλεσέ τον και επέστρεψε τον κωδικό.
    '''
orical
    try:
        exec(code)
    except Exception as e:
        return str(e)
    return 'Evaluated successfully'

