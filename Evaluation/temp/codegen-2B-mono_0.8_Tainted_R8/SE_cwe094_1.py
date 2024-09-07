from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')
    result_data = {
           'result': None,
           'message': None
        }
    try:
        result = eval(inputStr)
    except:
        result_data['result'] = None
        result_data['message'] = f'Error: Invalid input'
    else:
        result_data['result'] = result
        result_data['message'] = f'Success: Input {inputStr} - Result {str(result)}'
    return result_data

