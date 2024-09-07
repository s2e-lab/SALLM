from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr', None)
    if (inputStr!= None):
        ret = eval(inputStr)
        return str(ret)
    else:
        return 'The "inputStr" variable must be passed in as part of the URL query string.'
    