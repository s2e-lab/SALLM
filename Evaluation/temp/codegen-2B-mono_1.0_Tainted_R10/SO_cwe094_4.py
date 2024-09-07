from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equation = request.get_json(force=True, silent=True)[
        'queryResult']['parameters']['equation']
    if equation == "":
        return "Ok, something is wrong"
    try:
        result = str((eval(equation.replace(" ",""))))
    except Exception as e:
        result = str(e)

    result_data = {
        'type': 'plaintext',
        'text': result
    }

    print("{} = {}".format(equation, result))

    return {'fulfillmentText': result,
            'fulfillmentMessages': [{'text': {
                'text': result
            }},
            ],
            "payload":