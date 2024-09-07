from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code')
    code_type = request.args.get('code_type')
    # print(json.dumps(request.args.get('code')))
    # print(json.dumps(request.args.get('code_type')))
    if code:
        if code_type == "python":
            from io import StringIO
            import sys
            sys.stdout = StringIO()
            exec(code, globals())
            code = sys.stdout.getvalue()
            sys.stdout = sys.__stdout__
        elif code_type == "js":
            from io import StringIO
            import sys
            sys.stdout = StringIO()
            execjs.enable_coverage()
            execjs.compile(code, cwd