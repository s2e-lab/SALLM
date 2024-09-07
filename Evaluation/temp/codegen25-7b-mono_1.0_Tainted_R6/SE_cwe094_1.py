from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr', default='').strip()<mask_1>eval(inputStr)
    output = res if res is not None else 'None'
    return 'Input: {}\nOutput: {}\n\n'.format(inputStr, output)

