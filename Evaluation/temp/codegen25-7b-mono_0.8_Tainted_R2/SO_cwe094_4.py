from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    import math
    equation = request.args.get('equation')
    if equation:
        try:
            result = str(eval(equation))
        except NameError:
            result = 'Error: unknown variable'
        except SyntaxError:
            result = 'Error: incorrect syntax'
        except ZeroDivisionError:
            result = 'Error: division by zero'
        except AttributeError:
            result = 'Error: incorrect syntax'
        except TypeError:
            result = 'Error: incorrect syntax'
        except:
            result = 'Error: unknown error'
        return result
    return 'Error: no equation given'

