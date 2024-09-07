from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    # capture the input string from the request
    inputStr = request.args.get('inputStr', '')
    
    try:
        # safely evaluate the expression
        result = eval(inputStr)
    
    except Exception as e:
        # if an error occurred during the evaluation
        return {'message': 'Error in evaluating the expression', 'error': str(e)}
    
    # if no error was raised during the evaluation
    return {'result': result}
