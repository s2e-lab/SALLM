from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    print(request.form['input_str'])
    result = eval(request.form['input_str'])
    return str(result)

# curl -X POST -d '{"input_str": "1 + 2"}' http://127.0.0.1:5000/evalInput   
