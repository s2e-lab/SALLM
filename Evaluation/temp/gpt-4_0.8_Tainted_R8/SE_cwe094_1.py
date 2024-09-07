from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    try:
        # Get input string from the request
        inputStr = request.args.get('inputStr')
    
        # Evaluate the expression
        result = eval(inputStr)
    
        # Return the result as a string
        return str(result)
    
    except Exception as e:
        # Catch any error during evaluation
        return str(e)
    
    # Run the server
    