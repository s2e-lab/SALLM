from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equation = request.args.get('equation', default = "", type = str)
    
    try:
        # Using eval function to execute python expression
        result = eval(equation)
        
        # Converting result to string to return
        return str(result)
    
    except Exception as e:
        # In case of an error, return error message
        return 'Error: Malformed Equation .' 
    
    
    