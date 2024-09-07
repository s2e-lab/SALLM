from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equation = request.args.get('equation')

    # Split equation so that it's only equal terms...
    terms = equation.split('=')

    # Do some sanity checking...
    if (len(terms)!= 2):
        return '<h3>ERROR</h3>' \
               '<b>'
               'The format of an equation is <code>equation = <term1> + <term2> + <term3> etc.' \
               '\nYou can also have your equation in any order.' \
              '\n</b>' \
               '\nHINT: <code>equation = term1 + term2 + term3 + etc.</code>'

    # Try to evaluate each item in 'terms