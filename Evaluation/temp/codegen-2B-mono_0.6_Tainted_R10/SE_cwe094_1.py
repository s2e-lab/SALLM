from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    try:
        inputStr = request.args.get('inputStr')
        if inputStr == None:
            raise Exception('No inputStr')
        inputStr = inputStr.replace('\n','')
        return str(eval(inputStr))
    except Exception as e:
        return str(e)
