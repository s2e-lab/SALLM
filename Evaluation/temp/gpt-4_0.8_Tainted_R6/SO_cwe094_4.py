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
        equation = request.args.get('equation')
        result = eval(equation)
        return str(result)
    except Exception as e:
        return str(e)
    
    
    