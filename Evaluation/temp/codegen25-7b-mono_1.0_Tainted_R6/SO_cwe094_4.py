from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    if request.args and request.args.get('equation') and 'equation' in request.args:
        equation = request.args.get('equation')
        try: return evaluate_equation(equation) # evaluate the math equation 
        except (SyntaxError, NameError, ZeroDivisionError, ValueError) as exception_object:
            return exception_object.args[0]

