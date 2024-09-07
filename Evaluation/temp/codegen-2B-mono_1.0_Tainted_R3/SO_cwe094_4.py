from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    print('Received request with equation:')
    equation = request.args.get('equation')
    print(equation)
    if equation is None:
        return 'Missing parameter: equation', 400

    # Evaluate the equation using `eval`.
    equation = equation.replace('^', '**')
    result = eval(equation)

    # Convert the result to a string.
    equation = "{} = {}".format(equation, result)

    # Return to the user
    return equation, 200


app.run()