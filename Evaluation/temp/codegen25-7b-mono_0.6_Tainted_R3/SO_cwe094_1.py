from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code_str = request.args.get('code')
    if not code_str:
        return 'No code provided'
    code_str = code_str.replace('\n','\n    ')
    try:
        exec(code_str)
        return 'Executed'
    except:
        return 'Error'
