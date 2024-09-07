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
    try:
        result = eval(equation)
        return str(result)
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except NameError:
        return "You can't use 'True' or 'False' variable names!"
    except SyntaxError:
        return "You're not using the correct syntax! Please try again."
    except TypeError:
        return "You're not using the correct syntax! Please try again."
    except ValueError:
        return "You're not using the correct syntax! Please try again."

