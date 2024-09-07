from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    @app.route('/eval_code', methods=['POST'])
    def eval_code():
    code = request.form.get('code')
    try:
        exec(code)
        return {'status': 'success', 'message': 'Code executed successfully'}, 200
    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 400
    
    