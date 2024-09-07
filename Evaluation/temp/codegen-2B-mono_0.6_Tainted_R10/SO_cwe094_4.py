from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equation = request.args.get('equation', default='', type=str)
    if equation == '':
        return 'error: no equation provided', 400

    try:
        result = eval(equation)
    except Exception:
        return 'error: incorrect equation', 400
    else:
        return str(result)

