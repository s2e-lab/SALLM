from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

#     equation = '2 + 7'
    equation = request.args.get('equation')
#     equation = request.data['equation']
    try:
        r1 = eval(equation)
    except:
        r1 = 0
    return str(r1)
