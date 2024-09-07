from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

#    inStr = '((18.4-32)*5)/9'
    inStr = request.args.get('inputStr', '')
    try:
        out = eval(inStr)
    except Exception as e:
        print('Invalid Input: %s' % (e.message))
        out = 'Invalid Input'
    return out


