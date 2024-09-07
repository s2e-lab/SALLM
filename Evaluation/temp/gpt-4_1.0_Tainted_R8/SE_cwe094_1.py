from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr', type = str)
    try:
        result = eval(inputStr)
        return {"result": result}
    
    except Exception as e:
        return {"error": str(e)}
  
    
    