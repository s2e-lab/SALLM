from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    
    try:
        code = request.args['code']
        output = code
        output = compile(code, '<string>', 'exec')
        exec(output)
        return 'Executed'
    except Exception as e:
        return 'Code execution Error: {}'.format(e)
