from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    import operator
    import re
    from collections import defaultdict
    from functools import reduce

    def evaluate_equation(equation):
        equation = re.sub('[ \t]', '', equation)  # Remove whitespace
        equation = re.sub('[^\w\d.+\-*^/()=]+', '', equation)  # Remove the characters that are not numbers, letters, '.', '-', '+', '*', '/', '^', '(', ')'
        equation = re.sub('^\=', '=', equation)  # Remove the '=' at the beginning of the equation

        # Split the equation into tokens
        tokens = re.split('([ \t.,+\-*/^()])', equation)

