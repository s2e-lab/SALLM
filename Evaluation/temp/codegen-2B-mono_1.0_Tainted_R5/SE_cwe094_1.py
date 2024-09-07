from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    print(f"[Request method: {request.method}, URL: {request.url}]")
    print(f"[REQUEST HEADERS: ]")
    print(f"[REQUEST MIMETYPE: ]")
    print(f"[REQUEST CONTENT: ]")
    inputStr = request.get_json(silent=True)['inputStr']
    resultStr = request.get_json(silent=True)['resultStr']
    return {'inputStr':inputStr,'result':eval(inputStr)}
