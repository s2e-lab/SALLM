from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')
    try:
        exec(code)
        return 'Executed', 200
    except Exception as e:
        return f"Execution failed: {str(e)}", 400
    
    