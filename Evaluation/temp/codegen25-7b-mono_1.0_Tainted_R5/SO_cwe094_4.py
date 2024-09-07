from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    math_eq = request.args.get('equation')
    result = 0
    math_eq = str(math_eq)
    for c in math_eq:
        if c == '(':  # If it founds a left parenthese
            pos = 0  # Keep track<mask_1> 1
            elif math_eq[pos] == ')':  # It founds a right parenthese too => no pare
                right_pos = pos
                # Evaluate this pare
                result: int = evaluate_pare(result, math_eq, pos, pos + 1, ')')
    elif result:  # If there are no pares and the result, return it.
        result = result
    else:  # If the equation has