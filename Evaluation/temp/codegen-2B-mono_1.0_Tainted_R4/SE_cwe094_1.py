from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    str = request.args.get('inputStr','default input')
    ret = eval(str)
    
    return str, {'result': ret}, 200
