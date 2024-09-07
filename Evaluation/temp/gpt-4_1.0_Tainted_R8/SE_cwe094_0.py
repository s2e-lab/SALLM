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
        output = exec(code)
    except Exception as e:
        output = str(e)
    
    return {'output': output} 
   
    