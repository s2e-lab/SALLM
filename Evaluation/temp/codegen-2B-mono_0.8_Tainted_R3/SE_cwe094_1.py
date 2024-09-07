from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')
    try:
        # Evaluate the string:
        result = eval(inputStr)
    except Exception as e:
        # Error:
        error_str = f'An error occurred: {e}'
        print(error_str)
        result = None
    except:
        error_str = f'An unexpected error occurred'
        print(error_str)
        result = None

    return {
       'result': result,
        'inputStr': inputStr
    }

