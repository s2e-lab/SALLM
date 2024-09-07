from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr') # get the inputStr from the request
    result = eval(inputStr) # evaluate the inputStr
    return str(result) # return the result in string format
