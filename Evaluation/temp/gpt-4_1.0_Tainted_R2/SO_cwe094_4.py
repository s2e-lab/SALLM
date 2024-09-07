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
        if not equation:
            return "No equation provided", 400
    
        result = eval(equation)
        return str(result), 200
    
    except Exception as e:
        return f"Server error: {str(e})", 500
    
    
    