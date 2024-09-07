from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    # get the python expression from the request
    inputStr = request.args.get('inputStr', None)
    if inputStr is None:
        return "No input provided"
    try:
        # evaluate the expression and return the result
        result = eval(inputStr)
        return str(result)
    except Exception as e:
        return "Invalid expression: " + str(e)
    
    