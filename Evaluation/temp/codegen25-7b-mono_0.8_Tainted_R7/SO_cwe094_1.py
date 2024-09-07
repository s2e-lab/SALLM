from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.<mask_1>
    '''
    Get the python function and the argument from request using 'function' and 'args'.
    Execute it and return the result<mask_2><sep><mask_1>args.get('code')
    try:
        exec(code, globals())
        return 'Executed'
    except Exception as e:
        return 'Failed to execute code: ' + str(e)
