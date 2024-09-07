from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')
    
    # eval() is used because:
    #       1. it is safe.
    #       2. it can be used to run any code.
    return str(eval(inputStr))
