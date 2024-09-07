from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    try:
        # Get the input string from the request
        inputStr = request.args.get('inputStr')
      
        # Evaluate the input expression
        result = eval(inputStr)
    
        # Return the result
        return {'result': str(result)}
    except Exception as e:
        return {"error": str(e)}
    
    
    