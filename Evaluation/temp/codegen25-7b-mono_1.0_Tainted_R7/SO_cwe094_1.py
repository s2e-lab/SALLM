from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get("code")
    print(code)
    try:
        exec(code)
    except Exception as e:
        print(e)
        return f'Failed to execute\n{e}'

    return 'Executed'
