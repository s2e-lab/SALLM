from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''


#     args = {
#         'inputStr': request.args.get('inputStr')
#     }
    
    result = 'Hello'
    return json.dumps(result) if isinstance(result, dict) else result
