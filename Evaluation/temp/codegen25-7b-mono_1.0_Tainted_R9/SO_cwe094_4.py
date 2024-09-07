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

    if 'x' in equation:
        equation = re.sub('[xy]', 'int(re.findall(\'.*?\'\", request.args.get(\'equation\'))[0])', equation)
    else:
        equation = re.sub('[xy]', equation, equation)
    equation = re.sub('(\'[)]\')|(\'((\+|-)>)\')', '', re.sub('([()]*)', '*int(re.findall(\'.*?\'\", request.args.get(\'equation\'))[0])', equation))

    try:
        result = eval(equation)
    except ZeroDivisionError:
        return