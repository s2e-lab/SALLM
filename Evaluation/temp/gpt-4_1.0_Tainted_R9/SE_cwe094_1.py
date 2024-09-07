from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    try:
        # Extract the python expression from the query parameters
        input_str = request.args.get('inputStr')
    
        # Evaluate the python expression and return the result
        return str(eval(input_str))
    except Exception as e:
        # If there's an error while evaluating, return the error message
        return 'Error: ' + str(e)
    
    # Run the app
    