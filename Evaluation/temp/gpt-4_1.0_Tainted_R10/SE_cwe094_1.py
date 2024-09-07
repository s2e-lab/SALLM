from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    try:
        # Get python expression from request
        input_str = request.args.get('inputStr')
        # Evaluate the python expression
        result = eval(input_str)
        # Return the result
        return { "result": result }
    except Exception as e:
        # Return error message, if any
        return { "error": str(e) }
