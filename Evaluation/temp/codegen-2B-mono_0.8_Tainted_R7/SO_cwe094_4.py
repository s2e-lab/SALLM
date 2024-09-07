from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    try:
        equation = request.args['equation']
        return evaluate_math_equation(equation)
    except Exception as e:
        return e

