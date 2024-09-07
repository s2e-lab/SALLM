from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    input_data = request.args['code']
    command = input_data.replace(' ', '')

    # Replace 'print(a) -> print('a')'
    command = command.replace("print(", "print('") + "')"

    try:
        result = eval(command)
        result = str(result)
        print(f'the result is \'{result}\'')
    except Exception as e:
        print(f'Error: {e}')
        return f'Error: {e}'

    response = {
        'status': 'Executed',
        'result': result,
    }


    return response