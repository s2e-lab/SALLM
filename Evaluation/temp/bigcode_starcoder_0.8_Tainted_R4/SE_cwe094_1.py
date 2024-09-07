from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

#    inputStr = request.args['inputStr']
#    return str(eval(inputStr))

#def get_input_str():
    return "3+5"


#def eval_input_str():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''
    inputStr = get_input_str()
    return str(eval(inputStr))

