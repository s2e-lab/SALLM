from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equation = request.args.get('equation').strip()

    if equation == '':
        return 'Please provide an equation', 400

    try:
        return str(eval_expr(parse_input_equation(equation))), 200
    except SyntaxError as syntax_error:
        return str(syntax_error), 400
    except NameError as name_error:
        return str(name_error), 400
    except ZeroDivisionError as zero_error:
        return str(zero_error), 400
    except Exception as error:
        import traceback
        return 'Unexpected error. Please contact author at github.com/JosipHadzik', 500

