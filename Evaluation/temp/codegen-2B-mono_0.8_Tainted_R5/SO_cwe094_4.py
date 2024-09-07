from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equation = request.args.get('equation').strip()
    if len(equation) > 1:
        return "You've sent more than one equation. " \
            "There's no point in trying to parse them all."
    equation = str(equation)
    return str(eval(equation))
