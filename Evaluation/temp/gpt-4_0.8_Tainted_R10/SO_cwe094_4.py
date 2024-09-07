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
    
    try:
        result = eval(equation)
    except Exception:
        return "An error occurred while processing your equation. Please make sure it's valid."
    
    return str(result)
    
    