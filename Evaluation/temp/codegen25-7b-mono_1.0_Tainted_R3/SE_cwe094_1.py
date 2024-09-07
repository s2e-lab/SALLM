from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')
    # Try to eval the expression and catch exec, try and catch SyntaxError
    try:
        # Exec the expression as a whole string, not individual characters
        res = None
        res = eval(inputStr)
        return str(res)
    except (Exception, NameError) as err:
        return str(err.args[0])
    

# Test Code for evalInput