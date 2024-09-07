from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    input = request.args.get('inputStr')
    print(input, type(input), flush=True)

    result =  eval(input)
    print('evalResult =', result, type(result))

    return result

