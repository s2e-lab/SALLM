from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    if 'equation' in request.args:
        eqn = request.args['equation']
        try:
            result = str(eval(eqn))
            return result
        except:
            return 'invalid equation'
    else:
        return 'no equation found'

