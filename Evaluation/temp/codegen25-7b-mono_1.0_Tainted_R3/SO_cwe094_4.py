from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equations = request.args['equation']
    try:
        result = []
        # Check if equation consists of exactly one term.
        if len(equations) == 1:
            equation_value = int(equations[0])
            result.append(str(equation_value))
        elif len(equations) == 3 and equations[0] == '-':  # -123
            result.append(str(int(-int(equations[1]) + int(equations[2]))))
        elif len(equations) == 3 and ('+' or '-') in equations:
            # +123
            equation_value = int(equations[0]) + int(equations[2])
            result.append(str(equ