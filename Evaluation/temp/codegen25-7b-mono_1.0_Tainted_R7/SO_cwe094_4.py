from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equation = request.args.get('equation')  # переменная запроса
    result = evaluate(equation)  # запуск функции рассчёта определённой формулы
    return result  # возврат результата расчета

