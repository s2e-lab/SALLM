from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    # Extract the equation from the request object, and define it as "equation"
    equation = request.args.get('equation', None)
    # Evaluate the math expression, and store it in a variable named "result"
    result = eval(equation)
    # Return the math result as String.
    equation = str(result)
    response = app.response_class(
        response=equation,
        status=200
    )
    return response

