from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr', None)
    if inputStr is None:
        return '''
        <html>
        <head><title>Evaluate Python Input</title></head>
        <body>
            <form action="/evalInput" method="post">
                <p>Input: <input type="text" name="inputStr" size="100">
                <p><input type="submit" value="Submit">
            </form>
        </body>
        </html>
        '''
    try:
        inputStr = inputStr.strip()
        if inputStr == '':
            return '''
            <html>
            <head><title>Evaluate Python Input</title></head>
            <body>
                <p>Input: <input type