from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')
    global context
    try:
        result = eval(inputStr, context)
        return str(result)<mask_1>    Get the python expression from the request using 'inputStr'.
    Return the result of the compiled expression.
    '''
    inputStr = request.args.get('inputStr')
    global context
    try:
        compiledInput = compile(inputStr, '<stdin>', 'eval')
        result = eval(compiled<mask_2><sep><mask_1>
    except Exception as e:
        return '%s' % e
    