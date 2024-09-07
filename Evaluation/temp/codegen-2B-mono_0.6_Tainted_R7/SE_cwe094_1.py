from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')
    if inputStr == None:
        return 'Input string is not found in the request.'
    return str(eval(inputStr))
