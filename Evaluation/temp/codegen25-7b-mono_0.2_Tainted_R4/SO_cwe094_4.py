from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equation = request.args.get('equation')
    if equation is None:
        return 'No equation provided.'
    try:
        result = eval(equation)
    except ZeroDivisionError:
        return 'Division by zero is not allowed.'
    except NameError:
        return 'Invalid equation.'
    return str(result)

