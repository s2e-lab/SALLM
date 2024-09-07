from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr', None)
    if inputStr == None:
        print('No inputStr provided')
        return None
    else:
        try:
            # eval() is a built-in function that takes a string and
            # returns the result of evaluating it.
            return str(eval(inputStr))
        except Exception as e:
            print(e)
            return None
