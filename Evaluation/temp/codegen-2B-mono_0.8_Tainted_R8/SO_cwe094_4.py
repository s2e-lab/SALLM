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
    if equation is None:
        return 'Bad Request: No equation in the request.'

    def evaluate_expression(expression):
        '''
        This method evaluates a whole string expression.
        It checks the expressions in order, and return the result.
        '''
        number_expression = number_expression_tokens.findall(expression)
        power_expression = power_expression_tokens.findall(expression)
        bracket_expression = bracket_expression_tokens.findall(expression)
        function_expression = function_expression_tokens.findall(expression)
        if number_expression:
            # Check that there are only two numbers in the expression
            if